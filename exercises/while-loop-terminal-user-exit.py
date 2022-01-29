while True:
    try:
        # ask if continue playing
        user_input = int(input(f'Select Play Again = 0, Exit = 1 : '))
        
        if user_input: # če je user input karkoli drugega kot 0, je konec zanke
            print('uporabnik ne želi več igrati')
            break
    
    # if ctrl+c is pressed, exit game
    except KeyboardInterrupt as e:
        print('\nctrl+c was pressed.user exit')
        break