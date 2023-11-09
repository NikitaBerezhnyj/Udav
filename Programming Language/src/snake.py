import random
from colorama import Fore

def fill_terminal(version):
    rand_color_num = random.randrange(0, 5)
    if rand_color_num == 0:
        print(Fore.GREEN + f"""
                                                  
              .':ldxkOOOOOkdoc,.              
           ,lkOOOOOOOOOOOOOOOOOOOd:.          
        .oOOOOOOOOOkdoooodkOOOOOOOOOx:        
      .dOOOOOOOOOxloxkOOkxoldOOOOOOOOOOc      
     lOOOOOOOOOOo;oOOOxxOOOOd:OOOOOOOOOOk.    
    xOOOOOOOOOOx,,,cdcddllxxo:OOOOOOOOOOOO;   
   xOOOOOOOOOOOd,,;dllOOOkddxlcdOOOOOOOOOOO;  
  oOOOOOOOOOOOOO:dOOOdcdOOOOOkkOOOOOOOOOOOOO.       УДАВ
  OOOOOOOOOOOOOOkddkOOOc:dOOOOOOOOOOOOOOOOOOl       Версія: {version}
 .OOOOOOOOOkOOOOkkxclxx,,,:dkkkOOOOOOOOOOOOOO       Девіз: Удав - мова для тих,
 .OOOOOOOOco:kkcodddddddddollddldOOOOOOOOOOOO       хто боїться душити пітона
 .OOOOOOOx:O;kdcOOOOOOOOOc,,,;xdcOOOOOOOOOOOx        
  xOOOOOOcdO;lolll:::::loccccclloolkOOOOOOOO. 
  .OOOOOk;OO:kOOOOl;,,ckOOOOkc;;:ddcOOOOOOOd  
   .OOOOk:OOxloooooollllllooc;;;;;:lodOOOOx   
    .OOOOolkxlccdOOOOc,,,;xOOOOxlclxOllOOo    
      dOOOxl;,,,,lxxxxolldxxxxd,,,,,ocdO.     
        xOOOOkxxxxxxxxxxxxxxxxxxxxxxxO'       
          .OOOOOOOOOOOOOOOOOOOOOOOOx          
              cOOOOOOOOOOOOOOOOO       
    
        """)

    elif rand_color_num == 1:
        print(Fore.BLUE + f"""
                                                  
              .':ldxkOOOOOkdoc,.              
           ,lkOOOOOOOOOOOOOOOOOOOd:.          
        .oOOOOOOOOOkdoooodkOOOOOOOOOx:        
      .dOOOOOOOOOxloxkOOkxoldOOOOOOOOOOc      
     lOOOOOOOOOOo;oOOOxxOOOOd:OOOOOOOOOOk.    
    xOOOOOOOOOOx,,,cdcddllxxo:OOOOOOOOOOOO;   
   xOOOOOOOOOOOd,,;dllOOOkddxlcdOOOOOOOOOOO;  
  oOOOOOOOOOOOOO:dOOOdcdOOOOOkkOOOOOOOOOOOOO.       УДАВ
  OOOOOOOOOOOOOOkddkOOOc:dOOOOOOOOOOOOOOOOOOl       Версія: {version}
 .OOOOOOOOOkOOOOkkxclxx,,,:dkkkOOOOOOOOOOOOOO       Девіз: Удав - якщо ви не можете зламати
 .OOOOOOOOco:kkcodddddddddollddldOOOOOOOOOOOO       програму однією літерою, це не Удав
 .OOOOOOOx:O;kdcOOOOOOOOOc,,,;xdcOOOOOOOOOOOx        
  xOOOOOOcdO;lolll:::::loccccclloolkOOOOOOOO. 
  .OOOOOk;OO:kOOOOl;,,ckOOOOkc;;:ddcOOOOOOOd  
   .OOOOk:OOxloooooollllllooc;;;;;:lodOOOOx   
    .OOOOolkxlccdOOOOc,,,;xOOOOxlclxOllOOo    
      dOOOxl;,,,,lxxxxolldxxxxd,,,,,ocdO.     
        xOOOOkxxxxxxxxxxxxxxxxxxxxxxxO'       
          .OOOOOOOOOOOOOOOOOOOOOOOOx          
              cOOOOOOOOOOOOOOOOO       
    
        """)

    elif rand_color_num == 2:
        print(Fore.YELLOW + f"""
                                                  
              .':ldxkOOOOOkdoc,.              
           ,lkOOOOOOOOOOOOOOOOOOOd:.          
        .oOOOOOOOOOkdoooodkOOOOOOOOOx:        
      .dOOOOOOOOOxloxkOOkxoldOOOOOOOOOOc      
     lOOOOOOOOOOo;oOOOxxOOOOd:OOOOOOOOOOk.    
    xOOOOOOOOOOx,,,cdcddllxxo:OOOOOOOOOOOO;   
   xOOOOOOOOOOOd,,;dllOOOkddxlcdOOOOOOOOOOO;  
  oOOOOOOOOOOOOO:dOOOdcdOOOOOkkOOOOOOOOOOOOO.       УДАВ
  OOOOOOOOOOOOOOkddkOOOc:dOOOOOOOOOOOOOOOOOOl       Версія: {version}
 .OOOOOOOOOkOOOOkkxclxx,,,:dkkkOOOOOOOOOOOOOO       Девіз: Удав - мова програмування,
 .OOOOOOOOco:kkcodddddddddollddldOOOOOOOOOOOO       яка вас проковтне, якщо ви не будете її годувати
 .OOOOOOOx:O;kdcOOOOOOOOOc,,,;xdcOOOOOOOOOOOx        
  xOOOOOOcdO;lolll:::::loccccclloolkOOOOOOOO. 
  .OOOOOk;OO:kOOOOl;,,ckOOOOkc;;:ddcOOOOOOOd  
   .OOOOk:OOxloooooollllllooc;;;;;:lodOOOOx   
    .OOOOolkxlccdOOOOc,,,;xOOOOxlclxOllOOo    
      dOOOxl;,,,,lxxxxolldxxxxd,,,,,ocdO.     
        xOOOOkxxxxxxxxxxxxxxxxxxxxxxxO'       
          .OOOOOOOOOOOOOOOOOOOOOOOOx          
              cOOOOOOOOOOOOOOOOO       
    
        """)

    elif rand_color_num == 3:
        print(Fore.MAGENTA + f"""
                                                  
              .':ldxkOOOOOkdoc,.              
           ,lkOOOOOOOOOOOOOOOOOOOd:.          
        .oOOOOOOOOOkdoooodkOOOOOOOOOx:        
      .dOOOOOOOOOxloxkOOkxoldOOOOOOOOOOc      
     lOOOOOOOOOOo;oOOOxxOOOOd:OOOOOOOOOOk.    
    xOOOOOOOOOOx,,,cdcddllxxo:OOOOOOOOOOOO;   
   xOOOOOOOOOOOd,,;dllOOOkddxlcdOOOOOOOOOOO;  
  oOOOOOOOOOOOOO:dOOOdcdOOOOOkkOOOOOOOOOOOOO.       УДАВ
  OOOOOOOOOOOOOOkddkOOOc:dOOOOOOOOOOOOOOOOOOl       Версія: {version}
 .OOOOOOOOOkOOOOkkxclxx,,,:dkkkOOOOOOOOOOOOOO       Девіз: Удав - користуйся Удавом,
 .OOOOOOOOco:kkcodddddddddollddldOOOOOOOOOOOO       удуши в собі жабу
 .OOOOOOOx:O;kdcOOOOOOOOOc,,,;xdcOOOOOOOOOOOx        
  xOOOOOOcdO;lolll:::::loccccclloolkOOOOOOOO. 
  .OOOOOk;OO:kOOOOl;,,ckOOOOkc;;:ddcOOOOOOOd  
   .OOOOk:OOxloooooollllllooc;;;;;:lodOOOOx   
    .OOOOolkxlccdOOOOc,,,;xOOOOxlclxOllOOo    
      dOOOxl;,,,,lxxxxolldxxxxd,,,,,ocdO.     
        xOOOOkxxxxxxxxxxxxxxxxxxxxxxxO'       
          .OOOOOOOOOOOOOOOOOOOOOOOOx          
              cOOOOOOOOOOOOOOOOO       
    
        """)

    elif rand_color_num == 4:
        print(Fore.CYAN + f"""
                                                  
              .':ldxkOOOOOkdoc,.              
           ,lkOOOOOOOOOOOOOOOOOOOd:.          
        .oOOOOOOOOOkdoooodkOOOOOOOOOx:        
      .dOOOOOOOOOxloxkOOkxoldOOOOOOOOOOc      
     lOOOOOOOOOOo;oOOOxxOOOOd:OOOOOOOOOOk.    
    xOOOOOOOOOOx,,,cdcddllxxo:OOOOOOOOOOOO;   
   xOOOOOOOOOOOd,,;dllOOOkddxlcdOOOOOOOOOOO;  
  oOOOOOOOOOOOOO:dOOOdcdOOOOOkkOOOOOOOOOOOOO.       УДАВ
  OOOOOOOOOOOOOOkddkOOOc:dOOOOOOOOOOOOOOOOOOl       Версія: {version}
 .OOOOOOOOOkOOOOkkxclxx,,,:dkkkOOOOOOOOOOOOOO       Девіз: Удав - стань першим користувачем
 .OOOOOOOOco:kkcodddddddddollddldOOOOOOOOOOOO       Удава, не будь вужем
 .OOOOOOOx:O;kdcOOOOOOOOOc,,,;xdcOOOOOOOOOOOx        
  xOOOOOOcdO;lolll:::::loccccclloolkOOOOOOOO. 
  .OOOOOk;OO:kOOOOl;,,ckOOOOkc;;:ddcOOOOOOOd  
   .OOOOk:OOxloooooollllllooc;;;;;:lodOOOOx   
    .OOOOolkxlccdOOOOc,,,;xOOOOxlclxOllOOo    
      dOOOxl;,,,,lxxxxolldxxxxd,,,,,ocdO.     
        xOOOOkxxxxxxxxxxxxxxxxxxxxxxxO'       
          .OOOOOOOOOOOOOOOOOOOOOOOOx          
              cOOOOOOOOOOOOOOOOO       
    
        """)

    else:
        print(Fore.WHITE + f"""
                                                  
              .':ldxkOOOOOkdoc,.              
           ,lkOOOOOOOOOOOOOOOOOOOd:.          
        .oOOOOOOOOOkdoooodkOOOOOOOOOx:        
      .dOOOOOOOOOxloxkOOkxoldOOOOOOOOOOc      
     lOOOOOOOOOOo;oOOOxxOOOOd:OOOOOOOOOOk.    
    xOOOOOOOOOOx,,,cdcddllxxo:OOOOOOOOOOOO;   
   xOOOOOOOOOOOd,,;dllOOOkddxlcdOOOOOOOOOOO;  
  oOOOOOOOOOOOOO:dOOOdcdOOOOOkkOOOOOOOOOOOOO.       УДАВ
  OOOOOOOOOOOOOOkddkOOOc:dOOOOOOOOOOOOOOOOOOl       Версія: {version}
 .OOOOOOOOOkOOOOkkxclxx,,,:dkkkOOOOOOOOOOOOOO       Девіз: Удав - патріотичний плазун,
 .OOOOOOOOco:kkcodddddddddollddldOOOOOOOOOOOO       що допоможе привітатися з світом рідною мовою
 .OOOOOOOx:O;kdcOOOOOOOOOc,,,;xdcOOOOOOOOOOOx        
  xOOOOOOcdO;lolll:::::loccccclloolkOOOOOOOO. 
  .OOOOOk;OO:kOOOOl;,,ckOOOOkc;;:ddcOOOOOOOd  
   .OOOOk:OOxloooooollllllooc;;;;;:lodOOOOx   
    .OOOOolkxlccdOOOOc,,,;xOOOOxlclxOllOOo    
      dOOOxl;,,,,lxxxxolldxxxxd,,,,,ocdO.     
        xOOOOkxxxxxxxxxxxxxxxxxxxxxxxO'       
          .OOOOOOOOOOOOOOOOOOOOOOOOx          
              cOOOOOOOOOOOOOOOOO       
    
        """)

    print(Fore.WHITE)
