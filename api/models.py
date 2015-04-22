from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=64, null=True, blank=False)
    last_name = models.CharField(max_length=64, null=True, blank=False)
    
    # Preferences
    communication_options = ArrayField(models.TextField(), default=[])
    
    def add_communication_option(self, option, double_opt_in=False):
        option = option.strip()
        option_pending = "{0}:pending".format(option)
        if not (option in self.communication_options or option_pending in self.communication_options):
            if double_opt_in:
                self.communication_options.append(option_pending)
            else:
                self.communication_options.append(option)
                self.esl_update_required = True

    def remove_communication_option(self, option):
        option = option.strip()
        option_pending = "{0}:pending".format(option)

        if option in self.communication_options:
            self.communication_options.remove(option)
        if option_pending in self.communication_options:
            self.communication_options.remove(option_pending)

    def accept_communication_option(self, option):
        option = option.strip().replace(":pending", "")
        option_pending = option + ":pending"

        if option_pending in self.communication_options:
            idx = self.communication_options.index(option_pending)
            self.communication_options[idx] = option
