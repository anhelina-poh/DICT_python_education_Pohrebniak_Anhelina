
def  run_zoo_program():
    """
    Description:
    Runs the interactive zoo program. The user can enter a number to see the ASCII art of the corresponding animal habitat.
    Entering 'exit' terminates the program.

    Parameters:
    (No parameters)

    Returns:
    None: The program prints information directly to the console.
    """
    print("I love animals!"
          "\nLet's check out the animals!"
          "\nLet's check out the animals..."
          "\nThe deer looks fine."
          "\nThe lion looks healthy.")
    camel = r"""
    The camel habitat...
     ___.-''''-.
    /___  @    |
    ',,,,.     |         _.'''''''._
         '     |        /           \
         |     \    _.-'             \
         |      '.-'                  '-.
         |                               ',
         |                                '',
          ',,-,                           ':;
               ',,| ;,,                 ,' ;;
                  ! ; !'',,,',',,,,'!  ;   ;:
                 : ;  ! !       ! ! ;  ;   :;
                 ; ;   ! !      ! !  ; ;   ;,
                ; ;    ! !     ! !   ; ;
                ; ;    ! !    ! !     ; ;
               ;,,      !,!   !,!     ;,;
               /_I      L_I   L_I     /_I
    Look at that!"""
    lion = r"""
    The lion habitat...
                                                   ,w.
                                                 ,YWMMw  ,M  ,
                            _.---.._   __..---._.'MMMMMw,wMWmW,
                       _.-""        '''           YP"WMMMMMMMMMb,
                    .-' __.'                   .'     MMMMW^WMMMM;
        _,        .'.-'"; `,       /`     .--""      :MMM[==MWMW^;
     ,mM^"     ,-'.'   /   ;      ;      /   ,       MMMMb_wMW"  @\
    ,MM:.    .'.-'   .'     ;     `\    ;     `,     MMMMMMMW `"=./`-,
    WMMm__,-'.'     /      _.\      F'''-+,,   ;_,_.dMMMMMMMM[,_ / `=_}
    "^MP__.-'    ,-' _.--""   `-,   ;       \  ; ;MMMMMMMMMMW^``; __|
               /   .'            ; ;         )  )`{  \ `"^W^`,   \  :
              /  .'             /  (       .'  /     Ww._     `.  `"
             /  Y,              `,  `-,=,_{   ;      MMMP`""-,  `-._.-,
            (--, )                `,_ / `) \/"")      ^"      `-, -;"\:
    The lion is roaring!"""
    deer = r"""
    The deer habitat...
       /|       |\
    `__\\       //__'
       ||      ||
     \__`\     |'__/
       `_\\   //_'
       _.,:---;,._
       \_:     :_/
         |@. .@|
         |     |
         ,\.-./ \
         ;;`-'   `---__________-----.-.
         ;;;                         \_\ 
         ';;;                         |
          ;    |                      ;
           \   \     \        |      /
            \_, \    /        \     |\
              |';|  |,,,,,,,,/ \    \ \_
              |  |  |           \   /   |
              \  \  |           |  / \  |
               | || |           | |   | |
               | || |           | |   | |
               | || |           | |   | |
               |_||_|           |_|   |_|
              /_//_/           /_/   /_/
    Pretty good!"""
    goose = r"""
    The goose habitat...

                                        _
                                    ,-"" "".
                                  ,'  ____  `.
                                ,'  ,'    `.  `._
       (`.         _..--.._   ,'  ,'        \    \
      (`-.\    .-""        ""'   /          (  d _b
     (`._  `-"" ,._             (            `-(   \
     <_  `     (  <`<            \              `-._\
      <`-       (__< <           :
       (__        (_<_<          ;
        `------------------------------------------
    Beautiful!"""
    bat = r"""
    The bat habitat...
    _________________               _________________
     ~-.              \  |\___/|  /              .-~
         ~-.           \ / o o \ /           .-~
            >           \\  W  //           <
           /             /~---~\             \
          /_            |       |            _\
             ~-.        |       |        .-~
                ;        \     /        i
               /___      /\   /\      ___\
                    ~-. /  \_/  \ .-~
                       V         V
    It's doing fine."""
    rabbit = r"""
    The rabbit habitat...
           ,
          /|      __
         / |   ,-~ /
        Y :|  //  /
        | jj /( .^
        >-"~"-v"
       /       Y
      jo  o    |
     ( ~T~     j
       >._-' _./
      /   "~"  |
      Y     _,  |
     /| ;-"~ _  l
    / l/ ,-"~    \
     \//\/      .- \
     Y        /    Y
     l       I     !
     ]\      _\    /"\
     (" ~----( ~   Y.  )
    It looks fine!"""


    animals = [camel, lion, deer, goose, bat, rabbit]
    while True:
        user_input = input("Please enter the number of the habitat you would like to view: ")


        if user_input == 'exit':
            print("See you later!")
            break


        if user_input.isdigit():
            number = int(user_input)


            if 0 <= number < len(animals):
                print(animals[number])
            else:
                pass
        else:
            pass


if __name__ == "__main__":
        run_zoo_program()

