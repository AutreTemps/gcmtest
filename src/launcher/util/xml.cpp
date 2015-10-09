#include "launcher/util/xml.hpp"

#include <string.h>

#include <libxml/xpathInternals.h>

#include "libgcm/Exception.hpp"

xml::Doc::Doc(const xmlDocPtr doc): doc(doc)
{
    ctx = xmlXPathNewContext(doc);
}

xml::Doc::Doc(Doc&& d)
{
    doc = d.doc;
    d.doc = nullptr;
    ctx = xmlXPathNewContext(doc);
}

xml::Doc xml::Doc::fromFile(const std::string& fname)
{
    return Doc(xmlParseFile(fname.c_str()));
}

xml::Doc xml::Doc::fromString(const std::string& str)
{
    return Doc(xmlParseDoc((xmlChar*)str.c_str()));
}

xml::Doc::~Doc()
{
    if (doc) {
        xmlXPathFreeContext(ctx);
        xmlFreeDoc(doc);
    }
}

void xml::Doc::operator=(Doc&& d)
{
    xmlFreeDoc(doc);
    doc = d.doc;
    ctx = d.ctx;
    d.doc = nullptr;
    d.ctx = nullptr;
}

xml::Node xml::Doc::getRootElement() const
{
    return  Node(xmlDocGetRootElement(doc), ctx);
}

xml::Node::Node(const xmlNodePtr node, const xmlXPathContextPtr ctx): node(node), ctx(ctx)
{
    INIT_LOGGER("xml.Node");
}

std::string xml::Node::getTagName() const
{
    std::string name((char*) node->name);
    return name;
}

xml::NodeList xml::Node::getChildNodes() const
{
    NodeList nodes;
    for (xmlNodePtr child = node->children; child; child = child->next)
        if (child->type == XML_ELEMENT_NODE) {
            Node node(child, ctx);
            nodes.push_back(node);
        }
    return nodes;
}

xml::NodeList xml::Node::getChildrenByName(const std::string& name) const
{
    NodeList nodes;
    for (xmlNodePtr child = node->children; child; child = child->next)
        if (child->type == XML_ELEMENT_NODE && !strcmp((char*) child->name, name.c_str())) {
            Node node(child, ctx);
            nodes.push_back(node);
        }
    return nodes;
}

xml::Node xml::Node::getChildByName(const std::string& name) const
{
    NodeList nodes = getChildrenByName(name);
    auto l = nodes.size();
    if (l != 1) {
        LOG_ERROR("Expected one node with name " << name << " but found " << l);
        THROW_INVALID_ARG("Child not found");
    }
    return nodes[0];
}

xml::AttrList xml::Node::getAttributes() const
{
    xml::AttrList attrs;

    for (xmlAttrPtr attr = node->properties; attr; attr = attr->next) {
        std::string name((char*) attr->name);
        std::string value((char*) attr->children->content);
        attrs[name] = value;
    }

    return attrs;
}

xml::NodeList xml::Node::xpath(const std::string& expr) const
{
    xml::NodeList nodes;

    ctx->node = node;
    xmlXPathObjectPtr obj = xmlXPathEvalExpression((xmlChar*) expr.c_str(), ctx);

    if (!xmlXPathNodeSetIsEmpty(obj->nodesetval))
        for (int i = 0; i < obj->nodesetval->nodeNr; i++) {
            xmlNodePtr node = obj->nodesetval->nodeTab[i];
            if (node->type == XML_ELEMENT_NODE) {
                Node _node(node, ctx);
                nodes.push_back(_node);
            }
        }

    xmlXPathFreeObject(obj);

    return nodes;
}

std::string xml::Node::getTextContent() const
{
	auto content = (char*)xmlNodeGetContent(node);
    std::string res(content);
    free(content);

    return res;
}

std::string xml::Node::operator[](const std::string& name) const
{
    return getAttributeByName(name);
}

std::string xml::Node::getAttributeByName(const std::string& name) const
{
    auto attrs = getAttributes();
    auto iter = attrs.find(name);
    if (iter != attrs.end())
        return iter->second;
    THROW_INVALID_ARG("Attribute \"" + name + "\" not found in list and default value is not provided");
}

std::string xml::Node::getAttributeByName(const std::string& name, const std::string& defaultValue) const
{
    if (hasAttribute(name))
        return getAttributeByName(name);
    else
        return defaultValue;
}

bool xml::Node::hasAttribute(const std::string& name) const
{
    auto attrs = getAttributes();
    return attrs.find(name) != attrs.end();
}

void xml::Doc::registerNamespace(const std::string &prefix, const std::string &uri) {
    xmlXPathRegisterNs(ctx, (const xmlChar*)prefix.c_str(), (const xmlChar*)uri.c_str());
}
