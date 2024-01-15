# This is DMOJ problem wc16c1j1
# https://dmoj.ca/problem/wc16c1j1

# This is DMOJ problem wc18c3j1
# https://dmoj.ca/problem/wc18c3j1

# James has a can of leftover paint, containing P ( 1 ≤ P ≤ 100 ) litres of the stuff. When combined with his boundless collection of bottlecaps, this can result in some high-quality wares. When a bottlecap is artfully covered with B ( 1 ≤ B ≤ 100 ) litres of paint, it turns into a completely legitimate, Pokémon league-certified gym badge!

# James will produce as many badges as he can using the paint, using exactly B litres each. Pokémon trainers love their gym badges, so each such badge is sure to sell for D ( 1 ≤ D ≤ 100 ) Pokédollars.

# There might still be some extra paint left over, once there's not enough for another complete badge. However, there's no need for it to go to waste - James will sell any remaining paint at a rate of 1 Pokédollar per litre.

# How much money will James make for Team Rocket in total, from his sales of badges and leftover paint? Hopefully it'll be enough for at least a loaf of bread!

P = int(input())
B = int(input())
D = int(input())
left = (P % B)
total = ((P // B)*D) + left
print(total)
