import redis

r = redis.Redis(
    host ="redis-18099.c300.eu-central-1-1.ec2.cloud.redislabs.com",
    port=18099,
    password="CAYR9UQG6Cub1kLYMuuiZxqCrFKyk5lY"
)
avviopartita = int(input("Se vuoi avviare la partita nuova premi 1 \nse no premi 0: "))
if avviopartita == 1:
    r.set("Lakers", 0)
    r.set("Olimpia", 0)

while True:
    print("\n\n\n\n\n\n\nle squadre sono Lakers e Olimpia\n")
    print(f'Sono rispettivamente {int(r.get("Lakers"))} e {int(r.get("Olimpia"))}\n')
    sqd_input =input("Inserisci chi ha segnato: ")
    punti = int(input("Quanti punti ha fatto: "))
    if punti == 1:
        r.incr(sqd_input)
    elif punti == 3 or punti == 2:
        r.incrby(sqd_input, punti)
    else:
        while punti !=3 and punti !=1 and punti !=2:
            punti = int(input("Numero non valido, riscrivilo: "))
        r.incrby(sqd_input, punti)


    if sqd_input == ":q":
        break


