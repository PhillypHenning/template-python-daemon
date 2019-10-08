# ENTRY POINT TO THE SYSTEM. 

# Change 'print' to log for more rebust logging
import datetime
import time


class TemplateDaemon():

    def __init__(self, *args, **kargs):
        pass

    def run(self):
        print('DAEMON: starting')
        try:

            while True:
                try:
                    # CRITERIA FOR STARTING ADDED HERE
                    # Template case; It's 12:00 UTC
                    ok = False
                    ts = datetime.datetime.utcnow()
                    c_hour = 4
                    if ts.hour == c_hour:
                        ok = True 
                    
                    print('Current time is: [{}]'.format(ts))
                    if ok: 
                        print('DAEMON: beginning work')
                        # ...
                        print('DAEMON: work finished')

                except KeyboardInterrupt:
                    print('DAEMON: Interrupted')
                    continue

                except Exception as e:
                    print('DAEMON: An error occured: [{}]'.format(e))

                finally:
                    ok = False
                    time.sleep(600) # 10 minute sleep timer
        
        except Exception as e: 
            print('DAEMON: An error occured: [{}]'.format(e))

        finally:
            print('DAEMON: stopping')


if '__main__' == __name__:
    TD = TemplateDaemon()
    TD.run()
