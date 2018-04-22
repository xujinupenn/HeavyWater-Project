import logging
import logging.handlers
from csv_read import read_csv
from wsgiref.simple_server import make_server
from list_read import  list_read
import numpy as np
from learing import learn

# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Handler 
LOG_FILE = './sample-app.log'
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1048576, backupCount=5)
handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add Formatter to Handler
handler.setFormatter(formatter)

# add Handler to Logger
logger.addHandler(handler)

welcome = """
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
  <!--
    Copyright 2012 Amazon.com, Inc. or its affiliates. All Rights Reserved.

    Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance with the License. A copy of the License is located at

        http://aws.Amazon/apache2.0/

    or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
  -->
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <title>Welcome</title>
  <style>
  body {
    color: #ffffff;
    background-color: #E0E0E0;
    font-family: Arial, sans-serif;
    font-size:14px;
    -moz-transition-property: text-shadow;
    -moz-transition-duration: 4s;
    -webkit-transition-property: text-shadow;
    -webkit-transition-duration: 4s;
    text-shadow: none;
  }
  body.blurry {
    -moz-transition-property: text-shadow;
    -moz-transition-duration: 4s;
    -webkit-transition-property: text-shadow;
    -webkit-transition-duration: 4s;
    text-shadow: #fff 0px 0px 25px;
  }
  a {
    color: #0188cc;
  }
  .textColumn, .linksColumn {
    padding: 2em;
  }
  .textColumn {
    position: absolute;
    top: 0px;
    right: 50%;
    bottom: 0px;
    left: 0px;

    text-align: right;
    padding-top: 11em;
    background-color: #1BA86D;
    background-image: -moz-radial-gradient(left top, circle, #6AF9BD 0%, #00B386 60%);
    background-image: -webkit-gradient(radial, 0 0, 1, 0 0, 500, from(#6AF9BD), to(#00B386));
  }
  .textColumn p {
    width: 75%;
    float:right;
  }
  .linksColumn {
    position: absolute;
    top:0px;
    right: 0px;
    bottom: 0px;
    left: 50%;

    background-color: #E0E0E0;
  }

  h1 {
    font-size: 500%;
    font-weight: normal;
    margin-bottom: 0em;
  }
  h2 {
    font-size: 200%;
    font-weight: normal;
    margin-bottom: 0em;
  }
  ul {
    padding-left: 1em;
    margin: 0px;
  }
  li {
    margin: 1em 0em;
  }
  </style>
</head>
<body id="sample">
  <div class="textColumn">
    <h1>HeavyWater</h1>
    <p>Machine Learning Problem</p>
  </div>
  
  <div class="linksColumn"> 
    <h2>Your data set</h2>
    <ul>
<form action="form_action.asp" method="post">
  <p>Data: <input type="text" name="name" /></p>
  <input type="submit" value="Submit" />
</form>

    </ul>
  </div>
</body>
</html>
"""

def application(environ, start_response):
    path    = environ['PATH_INFO']
    method  = environ['REQUEST_METHOD']
    if method == 'POST':
        try:
            if path == '/':
                request_body_size = int(environ['CONTENT_LENGTH'])
                request_body = environ['wsgi.input'].read(request_body_size).decode()
                logger.info("Received message: %s" % request_body)
            elif path == '/scheduled':
                logger.info("Received task %s scheduled at %s", environ['HTTP_X_AWS_SQSD_TASKNAME'], environ['HTTP_X_AWS_SQSD_SCHEDULED_AT'])
        except (TypeError, ValueError):
            logger.warning('Error retrieving request body for async work.')
        request_body_size = int(environ['CONTENT_LENGTH'])
        request_body = environ['wsgi.input'].read(request_body_size).decode()
        request_list = str(request_body[6:])
        
        test = request_list.replace('+','.')
        request_word = test.split('.')

        item_list = list_read()
        item  = item_list.get_list()
        label =item_list.get_label()
        data = np.zeros((1,100))
        yy =0
        for i in item:
          data[0,yy]=request_word.count(i)
          yy =yy+1
        tty = learn(0,0)
        predict =tty.predict_model(data)

        #
        pre_list = list(predict[0])
        p1 ='<h1 align="center">'+label[pre_list.index(max(pre_list))] +'</h1>'
        word = '<hr align="center" width="100%" />'
        p1 =p1+word
        for i in range(len(label)):
          label[i] = label[i] + " : "+  str(predict[0,i])
        a  = '<br/>'.join(label)
        response = p1+a
    elif method == 'GET':
        try:
            if path == '/':
              response = welcome
            else :
                #request_body_size = int(environ['CONTENT_LENGTH'])
                #request_body = environ['wsgi.input'].read(request_body_size).decode()
                #path
              request_list = str(path[1:])
        
              test = request_list.replace('+','.')
              request_word = test.split('.')
              item_list = list_read()
              item  = item_list.get_list()
              label =item_list.get_label()
              data = np.zeros((1,100))
              yy =0
              for i in item:
                data[0,yy]=request_word.count(i)
                yy =yy+1
              tty = learn(0,0)
              predict =tty.predict_model(data)

              #
              pre_list = list(predict[0])
              p1 ='<h1 align="center">'+label[pre_list.index(max(pre_list))] +'</h1>'
              word = '<hr align="center" width="100%" />'
              p1 =p1+word
              for i in range(len(label)):
                label[i] = label[i] + " : "+  str(predict[0,i])
              a  = '<br/>'.join(label)
              response = p1+a              
                #########
        except (TypeError, ValueError):
            logger.warning('Error retrieving request body for async work.')
            response = 'error'
    else:
        response = welcome
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    #return [response]
    return [response.encode('utf8')]


if __name__ == '__main__':
    httpd = make_server('', 80, application)
    print("Serving on port 8000...")
    httpd.serve_forever()
