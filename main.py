
from app import app

import view

from scheduling import th

th.start()
if __name__ == '__main__':
   
    app.run()