# razer-profixer
Scan and delete XML files for Razer Synapse enabled devices that lack the &lt;ProfileName> tag, resulting in a list populated with undeletable blank spaces. This script fixes that.

Move this script to C:\programdata\razer\synapse\accounts\accountfolder\devices\yourdevicename\profiles and then run it from a command line using 'python prof_name_check.py' without the quotes, then follow the prompts to delete the corrupt XML files. This was written using Python3
