from selenium.webdriver.chrome.options import Options as OptionsChrome
from selenium import webdriver
from os.path import expanduser
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
import time

class DriverChrome:
    # driver selenium 
    def init_driver_chrome(self, headless=False, profile=True):
        """Inicilización driver and generate profile, large duration sesión """
        options = OptionsChrome()
        chromeProfilePath = None
        if headless:
            options.headless = True
        else:
            options.headless = False
            options.add_argument("--mute-audio")
        if profile:
            path_home = self.get_user_home_dir_path()
            if '/' in path_home:
                # path linux
                chromeProfilePath = path_home+"/.config/google-chrome/onpe-user-profile/"
            else:
                # path windows
                chromeProfilePath = path_home+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\onpe-user-profile"
            options.add_argument("user-data-dir=%s" % chromeProfilePath)
        return webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options) 

    def get_user_home_dir_path(self):
        """Functions return current path """
        return expanduser("~")    

    def send_error(self, error, f_func):
        """
        this function capture erros driver
        :param error: messaje error
        :param f_func: Name error
        """
        str_error = {
            'file': 'Chrome - func: %s' % (f_func,),
            'date_error': datetime.now(),
            'user_admin': self.user,
            'menssage': error
        }
        print('========================================================')
        print('file: ', str_error['file'])
        print('date_error: ', str_error['date_error'])
        print('user_admin: ', str_error['user_admin'])
        print('menssage: ', str_error['menssage'])
        print('========================================================')
        # self.start_travel_history()