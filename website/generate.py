import os
import sys
import codecs
import argparse

from scaffold import web
web.load_widgets('widgets')

from pages import web
from pages import header, footer

from config.settings import *


def examples():
    """ page for testing new components"""
    header()

    #this is as simple as you can get
    web.page.section('put some content on the page')

    #render to the template
    web.template.body.append(web.page.render())

    #finish of the page
    return footer()

def generate_rss():
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate static pages')
    parser.add_argument('--folder', dest='folder', default='./static/html/' ,nargs='?', help='output folder')

    #module, function, output file
    pages_list = (
        ('pages.homepage', 'index', 'index.htm'),
        ('pages.blog', 'index', 'blog.htm'),
        ('pages.chat', 'index', 'chat.htm'),
        ('pages.donate', 'index', 'donate.htm'),
        ('pages.competition', 'index', 'competition.htm'))

    args = parser.parse_args()

    for module, page, filename in pages_list:
        page_module = __import__(module, globals(), locals(), page)
        with codecs.open(args.folder + '%s' % filename, 'w', "utf-8") as fp:
            try:
                fp.write(getattr(page_module, page)().decode('utf-8'))
                print('Successfully Generated %s%s' % (args.folder, filename))
            except Exception as e:
                print('Failed to Generate %s%s' % (args.folder, filename))
                import traceback
                exc_type, exc_value, exc_traceback = sys.exc_info()
                traceback.print_tb(exc_traceback, limit=10, file=sys.stdout)
                
