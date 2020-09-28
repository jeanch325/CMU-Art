from cmu_112_graphics import *

def appStarted(app):
    app.iconRad = 30
    app.margin = 30

    app.swipe = False
    app.notifGone = False

    app.notifX0 = 30
    app.notifX1 = app.width - 30
    app.notifY0 = 200
    app.notifY1 = 275

    app.alertX0 = (app.width / 2) - 20
    app.alertX1 = (app.width / 2) + 20
    app.alertY0 = (app.height / 2) - 50
    app.alertY1 = (app.height / 2) + 50

    app.textAlert = 'We are experiencing trouble sending this message due to the apparent lack of network security around your planet but due to the urgency of the current circumstances we have elected to take the risk. If you are a nonhuman or a humannot a member of the UN, please disregard this message and pass it along to the correct audience. We have received your request and have thought it over but have regretfully come to the decision that as the Intergalactic Council of Life, we will not be granting your planet a position in the Bimillennial Transspacial Relocation Leap. We have been carefully observing the happenings of Earth since the last Leap to judge whether your life forms would have matured enough to reach a competent level, but yet again, you have failed. It is still very apparent that Earth has yet to be ready to interact with the rest of civilized life in the Milky Way. You are unable to use the minimum restraint, respect, empathy, and completely lack the emotional intelligence to coexist among yourselves, and this behavior is quite unacceptable for your species by itself, let alone with the rest of life in our galaxy. As life on Earth has yet to ever have met the standards to qualify for a spot in the Bimillennial Transspacial Relocation Leap, we trust that you will remember how to prepare for the Big Freeze as you have experienced in the past. We hope that in the next iteration of your planet’s reality, your life forms will learn better than yours in this current time. We wish you luck, and see you next millennia. '
    app.currentLine = 0
    app.deleteMess = False
    app.shake = 20

def keyPressed(app, event):
    if (event.key == 'Enter'):
        app.swipe = True   
    elif (event.key == 'Right'):
        if parceAlertText(app)[app.currentLine] == parceAlertText(app)[-1]:
            app.deleteMess = True
        else:
            app.currentLine += 1
    elif (event.key == "Left"):
        app.currentLine -= 1

def timerFired(app):
    if app.swipe:
        notifSwipe(app)


def notifSwipe(app):
    app.notifX0 += 50
    app.notifX1 += 50
    if app.notifX0 >= app.width:
        app.swipe = False
        app.notifGone = True

def parceAlertText(app):
    text = app.textAlert
    output = ''
    outputList = []
    lineNum = 0
    for i in range(len(text) + 1):
        if i < len(text):
            output += text[i].upper()
            if i % 35 == 0 and i != 0:
                output += '\n'
                lineNum += 1
                if lineNum % 20 == 0:
                    output += ';'
    for line in output.split(';'):
        outputList.append(line)

    return outputList



def drawNotif(app, canvas):
    canvas.create_rectangle(app.notifX0, app.notifY0, 
                            app.notifX1, app.notifY1,
                            fill='dark gray', width=0)
    canvas.create_text(app.notifX0 + 150, app.notifY0 + 25,
                        text='EMERGENCY ALERT', font= 'Monaco 30')
    canvas.create_text(app.notifX0 + 110, app.notifY0 + 55,
                        text='PRIVATE MESSAGE', font= 'Monaco 20')

def drawLockScreen(app, canvas):
    # time and date
    canvas.create_rectangle(0, 0, app.width, app.height, fill='gray')
    canvas.create_text(app.width/2, 100, text='1:07', 
                        font='Arial 80', fill='white')
    canvas.create_text(app.width/2, 160, text='Monday, September 28',
                        font='Arial 20', fill='white')
    # notification
    canvas.create_rectangle(app.margin, 290, 
                            app.width - app.margin, 365,
                            fill='dark gray', width=0)          
    # camera icon
    for i in range(1, 5, 3):
        camCentx = (app.width / 5) * i
        camCenty = (app.height - 100)
        canvas.create_oval(camCentx - app.iconRad, camCenty - app.iconRad, 
                            camCentx + app.iconRad, camCenty + app.iconRad, 
                            fill='dark gray', width=0)
        canvas.create_rectangle(camCentx - 15, camCenty - 15, 
                            camCentx + 15, camCenty + 15,
                            fill='white', width=0)
        canvas.create_oval(camCentx - 10, camCenty - 10,
                            camCentx + 10, camCenty + 10, 
                            fill='dark gray', width=0)


def drawAlert(app, canvas):
    #################################### HERE #################################
    #text1, text2 = parceAlertText(app)
    canvas.create_rectangle(0, 0, app.width, app.height, fill='black')
    # text
    canvas.create_text(app.width / 2, 100, 
                        text='URGENTMESSAGE',
                        fill='red', font='Monaco 50 bold')
    canvas.create_text(app.width / 2, app.height/2 + 40, 
                        text=parceAlertText(app)[app.currentLine], 
                        fill='red', font='Monaco 20 bold')

def drawBlackoutScreen(app, canvas):
    canvas.create_rectangle(31 + app.shake, 92 + app.shake, 500, 1376, fill='red')
    canvas.create_rectangle(4, 3 + app.shake, 498 + app.shake, 1265, fill='black')
    canvas.create_rectangle(0, 0, 287, 1100, fill='black')
    canvas.create_rectangle(178 + app.shake, 67, 346, 961, fill='red')
    canvas.create_rectangle(20 + app.shake, 109 + app.shake, 89 + app.shake, 1290, fill='black')
    canvas.create_rectangle(370 + app.shake, 234, 500 + app.shake, 576 + app.shake, fill='red')
    canvas.create_rectangle(90, 0 + app.shake, 309, 468 + app.shake, fill='red')
    canvas.create_rectangle(78 + app.shake, 70, 260 + app.shake, 890, fill='black')
    canvas.create_rectangle(209, 345 + app.shake, 678, 689 + app.shake, fill='red')
    canvas.create_text(0, 40, text='ERROR', font='Copperplate 90', fill='red')
    canvas.create_text(30, app.width, text='ERROR', font='Copperplate 160', fill='red')
    canvas.create_text(100, 300, text='ERROR', font='Copperplate 30', fill='red')
    canvas.create_text(200, 600, text='ERROR', font='Copperplate 200', fill='red')
    canvas.create_text(78, 90, text='ERROR', font='Copperplate 60', fill='red')
    canvas.create_text(289, 300, text='ERROR', font='Copperplate 200', fill='red')
    
def redrawAll(app, canvas):
    drawLockScreen(app, canvas)
    drawNotif(app, canvas)
    if app.notifGone:
        drawAlert(app, canvas)
    if app.deleteMess:
        drawBlackoutScreen(app, canvas)

runApp(width=500, height=1400)
