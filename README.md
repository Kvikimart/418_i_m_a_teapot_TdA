# 418_i_m_a_teapot_TdA
<h2>Decision log 1.0:</h2>

V první fázi jsme se zaměřili na vytvoření spolehlivého a rozšiřitelného základu, kterému rozumíme a orientujeme se v něm.

Tech stack: Rozhodli jsme se použít Tour de App template s pure JavaScriptem, python Flaskem a MySQL. Vybrali jsme tak na základě minulých zkušeností, jednoduchosti a bohaté dokumentace.

CI/CD: Nevyhovovalo nám automatické spouštění GitHub Actions Workflow při každém commitu na main branch, tak jsme uvažovali o vytvoření sekundární dev branch, na které bychom pracovali dokud bychom neměli výsledek, který jsme připraveni deploynout, ale nakonec jsme nechali pouze původní main branch, a místo on push triggeru jsme použili workflow_dispatch, takže když jsme připraveni deploynout další verzi, spustíme workflow manuálně. Pro naše použití zatím ideální.

Databáze: Dle zadání jsme vytvořili tabulku skrz Flask, uživatele, atd. Oveřili jsme funkce a zabezpečení.

API: Vytvořili jsme dva API endpointy, team a health. API endpointy jsme otestovali, ověřili správné chování a vracení správných informací.

Ostatní: Zaměřili jsme se i na detaily jako např. přidání MIT licence nebo zápis hesel a citlivých údajů v repozitáři přes Github secrets/proměnné místo hardcoded stringů.
===================================================================================================================================================================================================================================================


                         . .                         
                 ::-==============-::.               
              .-**+-.             .:=+=-.            
             -#*:                      -++:          
           .=*=                         .=*-         
           :*=.                          .=*:        
          .=*:                            :*=.       
          .=*:            ...             :+=.       
           :*=           :==-:            :+:        
           .==          ..=*=:.           ==.        
            :+.    .:::::--::::::::::.   .=:         
            .==:..::::-:::::::::::::::.::=-          
    :=*#*=:  .==-+**==---:::::::::-=+====:           
     .:===:.  .==++*********+***++=---:--.           
       :===:  .====+=======--:::--:-:::::.           
       :===- .:=====+===--==----::-:---:::.          
       ===--::=+==+=======-:-:::::---::::::          
      .==--:-======+=======-==---==-==---::.         
      .====--===+=++++=======-------------::         
       :======+=+===============--==-------:.        
        :-=====+++++=++================----:.        
           :=====++==+===================--:.        
           .:==++++===+=============-===--::.        
         ...:====++===================---:::         
  . .....:::::====+=============----=-=---:.         
.......:::::-==+*++==================-===-:.         
         ..::-=**%%%#****+*+++++++**###*=:.          
            ..::-=+**###%%%%%#%##**+=-:..            
                    ............                     
<img width="474" height="316" alt="image" src="https://github.com/user-attachments/assets/34b1deae-31f2-4e05-b0fa-3e1e0746c2e8" />
