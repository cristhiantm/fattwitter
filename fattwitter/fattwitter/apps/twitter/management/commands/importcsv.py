# coding: utf-8
from django.core.management.base import BaseCommand, CommandError
from optparse import make_option, OptionParser
from apps.twitter.models import Equivalence
import re 
import pprint 


class Command(BaseCommand):
  args = '<poll_id poll_id ...>'
  help = 'Import CSV '

  option_list = BaseCommand.option_list + (
    make_option
    (
      '--f', 
      '--file', 
      dest='path_to_file', 
      default=False,
      help="Import the CSV file to the database."
    ),
  )

  def __init__(self, *args, **kwargs):
    super(Command, self).__init__(*args, **kwargs)

  def handle(self, *args, **options):
    if options['path_to_file'] :
      self.parse()



  def parse(self):
    file = open('C:\Users\eduardo\Downloads\calories.csv')  

    for line in file:
      try:
        list_match = re.split(',',line.encode('utf-8'))
        pprint.pprint(list_match)
        equivalence = Equivalence()
        equivalence.product_name = list_match[0].strip()
        #import pdb; pdb.set_trace()
        if len(list_match[1]) > 0:
          equivalence.calories = float(list_match[1].strip())
        else:
          equivalence.calories = 0.0
        equivalence.save()
        print 'Inserted...'
      except Exception, e:
        print e.message



      

    

