"""
        IncludeUrlContentWiki macro for MoinMoin 1.8
        
        Get the content from an URL, process it as wiki markup, and return those
        formatted results. 
        
        I personally use this in cases where I have a web server
        process to dynamically generate content that relies on wiki
        features like macros, smileys, table layout rules, etc.
        
        Usage: [[IncludeUrlContentWiki( http://foo.com/wikimarkup )]]

        Changes:
          11/19/08: Made the read text into unicode so that when the imported text contains a macro,
                    wikiutils doesn't freakout (in function invoke_extension_function).
        
        Originally written by:
        2005-03-31 Steve Poole, stevep@wrq.com 
        
        Updated by:
        2008-11-19 Dexter Arver, http://moinmo.in/counterpoke
"""

import urllib
from MoinMoin import wikiutil
from MoinMoin.parser.text_moin_wiki import Parser as WikiParser

def execute( macro, url ):
    request = macro.request
    try:
        text = urllib.urlopen( url ).read()
    except IOError:
        text = "{{{ IncludeUrl failed on " + url + " }}}"
    text = unicode(text,encoding='utf-8',errors='replace')
    return wikiutil.renderText(request, WikiParser, text)

