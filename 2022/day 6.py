def part1(s):
    for i in range(4, len(s)):
        if len(set(s[i-4:i])) == 4:
            return i

def part2(s):
    for i in range(14, len(s)):
        if len(set(s[i-14:i])) == 14:
            return i

i = '''tzltzltthfthtdtstftbfbnffdjjvnvcccnznpndppsvvlnvlnvndntnllwffvwwcpwccssqbqnbbwzbwwfjjscspspfsfvvzjvvmjvjwjljbbbqtbbcqbccdqcdcpddnvnjvvqwwbrbggjllhbbzlblrrrcwwrfrmffgddfsddnqnqpnnmzzwlzwzqwqgqnngnfnvnhvvfnvvszzrbrqbqnbbrsbsvssgngwgqwqbqsbsvbbdvdfvdvbbqlqdlqdllnppwcclwlvwlwjlwwdjjjcschhhmrrnnrznzlnnwmnwnfngghngnpggmrrzrttdbdtddjhdhrrqddnhnjjntjtbtmtffwcfcnfcnfnjjfnjfjjhrhhgfgttgmttltfllfqfnqqcbbrlblrbrcrssrllhddmnddmcdddvttfdfqfmqqcncggczczdccvhcvcjvvgnnqttltcchzhjjwmmqvqtqnqbbhddcqdccnwccttgwwzssncncjjprjjpbprrndnrnrhnhrnhngnhhbjbccpmpmrppjvpjpqjjsvjjhttcclmmqzzlggtqqqgdqqbhhtmmqfmqmwmjwmjmmnsmsvsrrvpvhhtshhhmqmdqqqqlfffwgwhwjjrfjfmfrmffgzzjvzznqqwggcvcnvvcpvpjpjbpbrpbrrzhhcffqqlzzrmzrmzmzrrqdqrqnqrnrnqnrnsrrnjrrgllgqlljldjjmvvqbqhhsmsmddsfdddcmmphhtjhjzhjjjhcjjzppwhwvvdnvnvpnvnlnvnffrjjtzzdqzzngzgqghhmvvgwwqhwhlhvvfzzdpzddtbdtbtvtlvlqlllvvdvsdsslccbscsbbcggldlvvdccdscdsdzsddpggcfggnffpjpnpcncfcqqlvvszzbpbqbcqczcqzcqzqqlrlwwbgglrrbgbhhlbbsffrprtpppdwdhwhbbpssvbvnntbbfnfddmmfcfcjfftbfbdbccngcgjcjtjftjffrwwtwlwddczcnzczpzcpccrqcrczrzcrzzhnntgtqgtgztgzzcpphshwswfwqqnzngzzbpzzpqpzqznzdzmzqqjzzhnhvnnqjnnrdrcctdtppsffzvvwvbbpttsrsspsddfvvfllrtlljpjlplcctthbbgbqgbgmmpwpvvghvhfhwfwcwvwrvwrvvcgccdncddbmbmfmlffgqggrzgzhhzfzdfzfhhzdhzhjzjhhbffrtrjtthssbpspddpttrggdndsnnjwwzrwrvvmqvmvdvhvjvnnqmmhrhrzzzwttnftfddsdfsfjsjcccvhvgvgzvgzvzbvvhwhbbpccfjfllgmlggtbggdsgsmmmnznqnhqhrqhrrtthwhqqvzqvvvqgqffpvptvpvwvbvsscsnnhlnhhzrzjrjrllcffpqpbpsbbflblppqffbqqpttccdgcgdgfdfgdgjddjljpljppdspddflftllhchmcmwcwddrqqsdsswwmwwwjdjvdvwwcgcddmhhqtqvqmvvnffqppnvpphpnnshsmhmdhmdddlnlmnmsnnpttlfttnqnhqnqrnrddplplbpbdpdhppccbnbwwpwzwgwdgdnggcmmtnmnznmzmwmrmtrrjppjgjmggndgnnjzzrczzftztzgzvgvddgmdgmgpmmgjmmnrrmvmnvvhqqggsnnplnlnbbrcbbpphssnqsnspnncfchhvjjdjvjfjddbjbddhlllpdnrhtzhqpphzfbjclncdlrbtzhcwslpnstdvjslnzfrvfdlmpgpfhrqtjvqvjlqgdcjrbjtjrgvbfwjzsvrbmffnhvjqnshvdjbgwmpwlfjznngzpqbvlztnvgvjsnwvhpfwbhfsmjgwwjdrrwbtvpwtzvjfhwrmnrhdsvgpgdsfgndmffqfplsgjrsvztzlznqsrbldbmmhqmjtrzscrbwlpgztlrvllprnhzsvtnvwzmjwqhqpjqhntcrscwcdnwzpvbdczzcmzrmdwthdtszqzftcsfbwfqggpcntfrgwpmjpdzjnczwcjmdjnrqjfwqbznznmcdvzqlpqschnmcfqjjrjwfmqqftfdhdzffvshqbmrgrpvlgqcgsbsngttvcpjswdgrhbblrhjllfbzngqjzzbdwtnlnrbpftvwbmrhvcnntdrbvtrtpcsqdsrvpsgggfpwcbzhwhwmmmmmgjzgdtwnzjdwjfljghbjvjnsgshmdpztnbbrnwfvzhtzqpzttftdmcmqzlnrgncwwtpwqrgmpmwwchwhbbbblcndbsrrqtnztcmqhvdwfcswnswvhqdtqfdrhjgczqvrzqczmnpcgbwntjvlsfrzrrjtsvfzfmbwwsftwqvttpjvbggrlcspnfhwwmrhdbbhdcjvmrhppvcmtmfhszjlcjjsdqfvjttcmffwzfpmjmjzhcrqmhhwzhjlnwphvvhmrbllsvpjljthjndffrdbmdjncnmdtcwfwjdwnrdlvqsbzczlhwrtpnzfwzzwbrqpglgvrjsnsprvwszmlrjcdgzwchmcqrjdlzqfvqwwfszpptprhcfsdfcrnhvhgvcdwgnqzjtmgznltbjjqwzlljrqcmpdncshzvsmvjwlmvtwbtjcgmqfslvwcfqpljzdjmdvqjlztbsbshcwhlvzcmzljvrrhrbzwvthgtnszpcrrdwcmtdncdzlbdscfbhrlqttcfshqrsgvzhlcnvfhppdqvblsznmctftmnslwgbmbgshgwvmzpdnmqmjgqnvrwprmbzrdprrbcwnslczvzgnssjqqzdrlntrnsrgbjjcpqvnqwvnwgslchqzbphcqsbvgvwzlnsndfrhqjvtlnqpcsgswzfvhjmfgwgfvhjgzntdbztmjsbmtwlfmvvgvztvwwmqclcgctqbvljgfngcvfqlmmvqmbtrnnbhqjjndzqhvvdztjgvwgrtltfrlzrjcpgwvpqwmcwmqccjtjhhbrrqphlpljvhjzpdfcdsgzfpnzdzhfdqjsnrvmwstrmmwmlhbvrjbtnmvwcqnzqzzpwzjdnfhqwwlsvgnnjgffzcnrtbjfwllnrgppchqwnfpwpgnfbvwcbjrlscnwlswjmnrcrhtdhgpzvgtfcqzgqtwvlhrgbmjvvzhrlzfvmrdjjctvfwsgmjwbqslhmjlcvlwrdqfmbhcfrmrvqtslplwpsgrfmntmtvmvqttbspmftgqdzlcfplcvvfmmjttwqjpdtjzzsfjcprvbwdvfrpzddhwrlmsnpjzqgdlfdzvdjnjtgtfflzzvjlmnnvmglrptsnppwscznltcvzfjmwshnsqsvsjpqwsqlbwzslhgrdcbbvcjspqfntbcpwwrphgpmwbpqdcfvvtlsgpfshtcrdftsltwnbnmzfwcwlmrhlntmmnnpsdchvntcwbnmjdgwcmzzvbrhbdbmlgwppzwsqvcccdbfzfsfhtmbppnwbtjvrvjtmddhmrjdqgnmrnjjpqsgtbgcvtclzzstlpldtqbnnvqjfbjcfzblvcwhjphzcgwfljjhzzmwdcrzsssznztcwpjlbcffnlmsfjbmtvhhcljmtqdprdmdgwgpnnlmhgwpsgprfqnspmntrdjwjmrflsbfpqhzswbsrdbdhjmvtwmjjnmpllgfllzgwwmswjcmggbrvsbbhjmsdzzpbhbrlphwdsmjdzsqjfrmdmpljnwscjrhdvzqbhhvpmhwqfrrhzlncrrrzhmjdwqjcbsqjbhbdbjzpslrnnbzctnnlhqmqqbdzfbrpfgwsrdglnplpspnnqhtbhzhzgtchcbqcmmcmvlllczqbtmbstzmnlhhhbmmbtjwnbgwjbfhgvfhqlsgdnnrsgghjzjlqfwbbgztdqzbhhwhcwtjwsgstjpzcjjvqbpfpvlqfqshvfzbwmfcwfgqvgmbppfvzgzznzhsqbvzlztsnmnrbgqzbmbhlvqhfncdfcpttgzpvvzdbhvqdtqsblqvrsrnmsfbqhrpvlzffdzptzghvmbmdzjrsqzhqddqm'''

print(part1(i))
print(part2(i))