## =================================================================== ##
#  this is file admin.py, created at 25-Oct-2011                #
#  maintained by Gustavo Rabello dos Anjos                              #
#  e-mail: gustavo.rabello@gmail.com                                    #
## =================================================================== ##

from polls.models import Poll
from django.contrib import admin

class PollAdmin(admin.ModelAdmin):
 fields = ['pub_date', 'question']

admin.site.register(Poll)



