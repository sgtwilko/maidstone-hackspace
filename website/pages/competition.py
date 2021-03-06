from pages import web
from pages import header, footer

features = [
    ('1 x Arduino UNO R3 development board',),
    ('1 x USB cable',),
    ('1 x Prototype extension board',),
    ('1 x Mini breadboard',),
    ('1 x 5V stepper motor',),
    ('1 x 2003 stepper motor driver board',),
    ('5 x Red LED',),
    ('5 x Green LED',),
    ('5 x Yellow LED',),
    ('2 x Vibration Sensor',),
    ('1 x Flame sensor',),
    ('1 x LM35 temperature sensor',),
    ('1 x Infrared receiver',),
    ('3 x Photoresistor',),
    ('4 x Key cap',),
    ('4 x Key switch',),
    ('1 x Adjustable potentiometer',),
    ('1 x Passive buzzer',),
    ('1 x Active buzzer',),
    ('1 x Jumper cap',),
    ('1 x Large breadboard',),
    ('1 x Remote Control',),
    ('1 x 1602 Screen',),
    ('1 x 9G servos',),
    ('1 x Component box',),
    ('1 x 10p DuPont line',),
    ('30 x Breadboard line(approximately)',),
    ('1 x 220ohm resistance',),
    ('1 x 8*8 dot matrix',),
    ('1 x One digit eight segment tube',),
    ('1 x Four digit eight segment tube',),
    ('1 x IC 74HC595',),
    ('1 x Battery Holder',),
    ('1 x 1K resistor plug',),
    ('1 x 10K resistor plug',),
    ('1 x 9V battery',),
    ('1 x 2.54mm 40pin pin header',)]


def index():
    """ page for testing new components"""
    web.template.create(title="Maidstone Hackspace - Screw sorting competition")
    header('Maidstone Hackspace - Competition')
    
    web.page.create(
        web.images.create(
            image='/static/images/competitions/screw_sorting_competition_banner.jpg',
            title="Screw sorting competition banner"
        ).add_attributes('align', 'middle'
        ).add_attributes('style', 'margin:auto;display:block;width:500px;'
        ).render())

    web.paragraph.create(
        """Welcome to the first Maidstone Hackspace challenge! A great opportunity for all  to show off their creative flair and to join our community of makers, tinkerers, artists and more.""")
    web.page.section(web.paragraph.render())

    web.page.append(web.title.create('The Challenge:').render())
    web.paragraph.create(
        """Design a device which can sort a jar of screws by size, the winning entry will be built by Maidstone Hackspace.""").render()
    web.page.section(web.paragraph.render())
    web.paragraph.create(
        """Concepts can be designed in any software as long as the finished product is viewable without any specialist software e.g.JPG images. If you prefer to paint or draw we accept that too.""")
    web.page.section(web.paragraph.render())
    web.paragraph.create(
        """Submissions must be via our mailing list. The closing date is the 31st of July, submissions after this date will not be entered.""")
    web.page.section(web.paragraph.render())

    web.paragraph.create(
        web.link.create('Submit your image here.', 'Submit your image here.', 'https://groups.google.com/forum/#!forum/maidstone-hackspace').render())
    web.page.section(web.paragraph.render())


    web.page.section(web.title.create('Win a UNO Basic Starter Kit', 2).render())

    web.paragraph.create(
        web.images.create(
            image='http://imgapp.banggood.com/thumb/large/2014/xiemeijuan/03/SKU208787/SKU208787a.jpg',
            title="Arduino starter kit"
        ).add_attributes('align', 'middle'
        ).add_attributes('style', 'margin:auto;display:block;width:500px;'
        ).render())

    web.paragraph.append(
        """This kit comes with an arduino board and various sensors and components, list below of every thing in the kit.""")

    web.list.create(ordered=False).set_classes('bullet-list')
    web.list * features
    web.paragraph.append(
        web.list.render())
    web.page.section(web.paragraph.render()) 

    #render to the template
    web.template.body.append(web.page.render())

    #finish of the page
    return footer()
