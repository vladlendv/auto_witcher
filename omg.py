from ahk import AHK
import time
ahk = AHK()

BLUE_COIN = '0x043851' # color for my turn
END_COLOR = '0x37271C'
DRAFT_COLOR = '0x004130'
CURRENT_COLOR = '0x000000' # check current coin color
firstStep = False
COUNTER = 5

time.sleep(3) # time before the script start
# ahk.click(500, 460) # enter in game menu

while COUNTER > 0:
  print('[start]')
  # START THE GAME *******************
  ahk.click(400, 460) #click on play

  # CARD DRAFT ROUND 1 ********************
  while CURRENT_COLOR != DRAFT_COLOR: # check coin colors, if not blue waiting more time
    time.sleep(3)
    CURRENT_COLOR = ahk.pixel_get_color(252, 445)

  CURRENT_COLOR = '0x000000'
  time.sleep(2)
  # draft some card
  ahk.key_press('Space')
  ahk.key_press('Enter')
  ahk.key_press('Enter')
  print('END DRAFT')

  ahk.click(550, 710) # finish card draft
  time.sleep(1)
  ahk.click(590, 445) # click yes

  time.sleep(15)

  if ahk.pixel_get_color(1234, 436) == BLUE_COIN:
    firstStep = True

  # WAIT FOR YOUR TURN 1 ************************
  while CURRENT_COLOR != BLUE_COIN: # check coin colors, if not blue waiting more time
    time.sleep(3)
    CURRENT_COLOR = ahk.pixel_get_color(1234, 436)

  CURRENT_COLOR = '0x000000'
  time.sleep(3)
  print('YOUR TURN')

  # START YOUR TURN 1 DROP THE CARD ON THE TABLE
  ahk.mouse_move(642, 407, speed=5)
  ahk.click() # open stard card on the table
  ahk.mouse_move(684, 673, speed=5)
  time.sleep(1)
  ahk.click()
  ahk.key_press('Enter')
  time.sleep(3)
  ahk.key_press('Enter')
  time.sleep(2)
  ahk.key_press('Enter')
  time.sleep(2)
  ahk.key_press('Enter')
  time.sleep(2)
  ahk.key_press('Space')

  # WAIT FOR YOUR TURN 2 ************************
  while CURRENT_COLOR != BLUE_COIN: # check coin colors, if not blue waiting more time
    time.sleep(3)
    CURRENT_COLOR = ahk.pixel_get_color(1234, 436)

  CURRENT_COLOR = '0x000000'
  time.sleep(3)
  print('YOUR TURN')


  # START YOUR TURN 2 DROP THE CARD ON THE TABLE
  ahk.mouse_move(684, 673, speed=5)
  time.sleep(1)
  ahk.click()
  ahk.key_press('Enter')
  time.sleep(3)
  ahk.key_press('Enter')
  time.sleep(2)
  ahk.key_press('Enter')
  time.sleep(2)
  ahk.key_press('Enter')
  time.sleep(2)
  ahk.key_press('Space')


  # WAIT FOR YOUR TURN 3 ************************
  while CURRENT_COLOR != BLUE_COIN: # check coin colors, if not blue waiting more time
    time.sleep(3)
    CURRENT_COLOR = ahk.pixel_get_color(1234, 436)

  CURRENT_COLOR = '0x000000'
  time.sleep(3)
  print('YOUR TURN')

  # START YOUR TURN 3 DROP THE CARD ON THE TABLE
  ahk.mouse_move(39, 601, speed=5)
  ahk.click() # use leader skill
  ahk.key_press('Space')
  time.sleep(1)
  ahk.key_press('Enter')
  time.sleep(2)
  ahk.key_press('Enter')
  time.sleep(2)
  ahk.key_press('Enter')
  time.sleep(4)
  ahk.mouse_move(684, 673, speed=5)
  time.sleep(1)
  ahk.click()
  ahk.key_press('Enter')
  time.sleep(3)
  ahk.key_press('Enter')
  time.sleep(2)
  ahk.key_press('Enter')
  time.sleep(2)
  ahk.key_press('Enter')
  time.sleep(2)
  ahk.key_press('Space')

  # WAIT FOR YOUR TURN 4 ************************
  while CURRENT_COLOR != BLUE_COIN: # check coin colors, if not blue waiting more time
    time.sleep(3)
    CURRENT_COLOR = ahk.pixel_get_color(1234, 436)

  CURRENT_COLOR = '0x000000'
  time.sleep(3)
  print('YOUR TURN')


  # PASS ON 7 CARDS ************************
  ahk.key_down('Space', blocking=False) # pass start
  time.sleep(2) # time for click 2 second
  ahk.key_up('Space') # end of click pass key



  # ROUND 2 *******************************
  # CARD DRAFT ROUND 2 ********************
  while CURRENT_COLOR != DRAFT_COLOR: # check coin colors, if not blue waiting more time
    time.sleep(3)
    CURRENT_COLOR = ahk.pixel_get_color(252, 445)

  CURRENT_COLOR = '0x000000'
  time.sleep(3)
  # draft some card
  ahk.key_press('Space')
  ahk.key_press('Enter')
  ahk.key_press('Enter')
  print('END DRAFT')

  ahk.click(550, 710) # finish card draft
  time.sleep(1)
  ahk.click(590, 445) # click yes

  time.sleep(15)

  # WAIT FOR YOUR TURN 1 ************************
  while CURRENT_COLOR != BLUE_COIN: # check coin colors, if not blue waiting more time
    time.sleep(3)
    CURRENT_COLOR = ahk.pixel_get_color(1234, 436)

  CURRENT_COLOR = '0x000000'
  time.sleep(3)
  print('YOUR TURN')


  # START YOUR TURN 1 DROP THE CARD ON THE TABLE
  ahk.mouse_move(684, 673, speed=5)
  time.sleep(1)
  ahk.click()
  ahk.key_press('Enter')
  time.sleep(3)
  ahk.key_press('Enter')
  time.sleep(2)
  ahk.key_press('Enter')
  time.sleep(2)
  ahk.key_press('Enter')
  time.sleep(2)
  ahk.key_press('Space')


  # WAIT FOR YOUR TURN 2 ************************
  while CURRENT_COLOR != BLUE_COIN: # check coin colors, if not blue waiting more time
    time.sleep(3)
    CURRENT_COLOR = ahk.pixel_get_color(1234, 436)

  CURRENT_COLOR = '0x000000'
  time.sleep(3)
  print('YOUR TURN')

  # START YOUR TURN 2 DROP THE CARD ON THE TABLE
  ahk.mouse_move(684, 673, speed=5)
  time.sleep(1)
  ahk.click()
  ahk.key_press('Enter')
  time.sleep(3)
  ahk.key_press('Enter')
  time.sleep(2)
  ahk.key_press('Enter')
  time.sleep(2)
  ahk.key_press('Enter')
  time.sleep(2)
  ahk.key_press('Space')


  # PASS ************************
  ahk.key_down('Space', blocking=False) # pass start
  time.sleep(2) # time for click 2 second
  ahk.key_up('Space') # end of click pass key


  # FORCED END GAME 
  # if (END_COLOR != CURRENT_COLOR):
  #   ahk.key_press('Escape')
  #   ahk.click(591, 433) #click on end yes  

  # WAIT FOR FINISH BUTTON ************************
  while CURRENT_COLOR != END_COLOR: # check coin colors, if not blue waiting more time
    time.sleep(5)
    # CHECK ROUND 3 OPTIONAL AND DRAFT THEN
    if ahk.pixel_get_color(252, 445) == DRAFT_COLOR:
      # CARD DRAFT ROUND 3 ********************
      time.sleep(3)
      # draft some card
      ahk.key_press('Space')
      time.sleep(1)
      ahk.key_press('Enter')
      time.sleep(1)
      ahk.key_press('Enter')
      print('END DRAFT')

      ahk.click(550, 710) # finish card draft
      time.sleep(1)
      ahk.click(590, 445) # click yes

      time.sleep(15)

    # WAIT FOR YOUR TURN 1 ************************
    while CURRENT_COLOR != BLUE_COIN: # check coin colors, if not blue waiting more time
      time.sleep(3)
      CURRENT_COLOR = ahk.pixel_get_color(1234, 436)

    CURRENT_COLOR = '0x000000'
    time.sleep(3)
    print('YOUR TURN')

    # START YOUR TURN 1 DROP THE CARD ON THE TABLE
    ahk.mouse_move(684, 673, speed=5)
    time.sleep(1)
    ahk.click()
    ahk.key_press('Enter')
    time.sleep(3)
    ahk.key_press('Enter')
    time.sleep(2)
    ahk.key_press('Enter')
    time.sleep(2)
    ahk.key_press('Enter')
    time.sleep(2)
    ahk.key_press('Space')


    # WAIT FOR YOUR TURN 2 ************************
    while CURRENT_COLOR != BLUE_COIN: # check coin colors, if not blue waiting more time
      time.sleep(3)
      CURRENT_COLOR = ahk.pixel_get_color(1234, 436)

    CURRENT_COLOR = '0x000000'
    time.sleep(3)
    print('YOUR TURN')


    # PASS AND FINISH ************************
    ahk.key_down('Space', blocking=False) # pass start
    time.sleep(2) # time for click 2 second
    ahk.key_up('Space') # end of click pass key
    CURRENT_COLOR = ahk.pixel_get_color(607, 713)

  CURRENT_COLOR = '0x000000'
  time.sleep(3)
  ahk.click(635, 635)
  time.sleep(1)
  ahk.click(607, 713)
  time.sleep(1)
  ahk.click(566, 715)
  COUNTER -= 1
  print('[end of the game]')
  print(COUNTER, ' games left')
  time.sleep(7)

print('Congratulations! Games completed')




  # ahk.mouse_move(1230, 393)



  # ahk.key_press('Escape')
  # ahk.click(591, 433) #click on end yes
  # time.sleep(20)
  # ahk.click(635, 635)
  # time.sleep(1)
  # ahk.click(640, 717)
  # time.sleep(3)
  # ahk.click(566, 717)
  # time.sleep(8)