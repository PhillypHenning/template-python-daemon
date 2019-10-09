# ENTRY POINT TO THE SYSTEM. 
# Change 'print' to log for more robust logging

import datetime
import time


class TemplateDaemon():

    def __init__(self, *args, **kargs):
        pass

    def run(self):
        print('DAEMON: starting')
        try:
            run_day = None
            while True:
                try:
                    # CRITERIA FOR STARTING ADDED HERE
                    # Template case; It's 12:00 UTC
                    ok = False
                    ts = datetime.datetime.utcnow()
                    current_day = ts.today().strftime('%m%d%Y')
                    c_hour = 4
                    if ts.hour == c_hour and run_day != current_day:
                        ok = True 

                    elif run_day == current_day: 
                        print('DAEMON: already ran today')
                    
                    if ok: 
                        run_day = current_day
                        print('DAEMON: beginning work')
                        # ...
                        print('DAEMON: work finished')

                except Exception as e:
                    print('DAEMON: An error occured: [{}]'.format(e))

                finally:
                    ok = False
                    time.sleep(10) # 10 minute sleep timer
        
        except Exception as e: 
            print('DAEMON: An error occured: [{}]'.format(e))
        
        except KeyboardInterrupt:
            print('DAEMON: Interrupted')

        finally:
            print('DAEMON: stopping')


if '__main__' == __name__:
    TD = TemplateDaemon()
    TD.run()
