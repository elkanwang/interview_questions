'''
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.

'''

from sets import Set


def doWeShare(word1, word2):
    chars = Set()
    for char in word1:
        chars.add(char)
    for char in word2:
        if char in chars:
            return False
    return True


def maxProduct(words):
    wordsLength = len(words)
    tempRes = 0
    for i in range(wordsLength):
        for j in range(i, wordsLength):
            if doWeShare(words[i], words[j]):
                tempRes = max(len(words[i]) * len(words[j]), tempRes)
    return tempRes


sample1 = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
sample2 = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
sample3 = ["a", "aa", "aaa", "aaaa"]
sample4 = ["gdocnidllpfeiidcbkmcnjpekdddmochfeejiigdheajakbgomaailgpkkbjklkjphgdiakapemgpgabghlljfmjbbpapaefkjdak","dhcknhfdbkailejimmfgdaglhjbcifolgpfaaejkmkelanag","agpefkipapiaenhcbglgnjhiebkgfghlfejiaooknboecjlffoofioeeghmedbegjamifldlom","gljkghbjbhkkgileinhbbkchphhhc","pfholmojemdpnbampchnlah","fbnonaocgbdoagkbjlmhkbheepofcacmaflelambcgpnjfjeplgjbmncibdgenjkjgmfgog","ekonfgmjandiokigkgmpmeaadeheel","agpaomhhlppdonpcjfipmlekpjnhnjokblknjklkfacagjjejpkbkefdfclgfnkpjocmaj","fhlopfbmfkpkcafliplkpbfjhgfndcnfeokmodpiobm","elboldogngpdmlildkjnmomojdibpdncopjaacjjocjoncginloknajbnnlmocfckhphldfkmphanloo","hjdifjnakflcpcbeekhcoebohgbdhodjn","kilhmlkmmmbcimagjgm","jookcalodcfjiegldblk","dpdppeenkalkfgklkjccifbddlmageokiepcgkgaccp","jgbcdgoplockhfmecfb","ceonaenpjoebnfmdnnjbamccjbhmnpaoaolcjekdohpclajojcgcmhcaiphkoleggeecheceimhaiepmiimegaajdcj","ckklhboflogekfncahibonfomeikgjo","eibmfkldplkkmiilidfpdnkchgeghiedkbfenjdmdnnoihobdaomgaengfepbedmmconjcaeghnokcdcabib","icgjcdjpjmgidmahcfffjjijicpbmkebohiajbfjhcbaeodgemoocnmhenellllfonfplkoocak","pmpejblbjkehmgibhmnfocoljlhbihnekcgpgejmnhofbpldgibioakniiiceep","mmkjnmfllaeooehlhhlejedbbpjipapmbfpibgcdmcji","lepedhdcdmlhpnpialcffaplidpflbkdbnpam","mfihoplepleilkcgfjmcjgmbodkhgfkpkdcjlkhoieghehcpmakpdfgkffmmohohpmebjpenmifnphnlpifaolonlc","dbgmecldegbhnjdbmbb","dpcdfblbddiiemijiddbfoibbojmmkcnppcbjcoafifk","fhndcbpbnnlinjlcipnnjikocdikjbijpinkphhmhpianbcacdnelkllkoinghbdbhkjogiegkpihpbllpplamend","nphbhjkeaablhgifopmnfikbekehfjoobmkaphoodkiigoocfkbaokihjamlbbbpme","fafhamofldpbnbpfdjacjgnacind","jpckingakeofoijbjnjlpoaomlhlblncaiciibelmcfhaagomhklggmpfidlfbconencpgj","pmgiejneeijklljmhfanfnndhabkajkecmcldegkjnabnldodfhhplicmkgibaajladebdnbbbmmjlnlnmpaicglhpgpefp","jiacoojabpgieligpedpfmjhmfffeii","fcfjleennidcngccdphpdekfebhimdfekkljfdcodcffpjdogkahcjjjkacbimmockoeobabcikgpfdifnpogcfeamcnpljb","adeboflmaghdadkhpngpppndmlinikdfheccgdephjjkcojjmipfkhnkjdohnfbmglp","modfcdkmgmnkmdcpaoakngbonekchpclndhmepijnhgmmgimignac","egjflmpchnmfhghfldcnpandaefohnmjlnkpdobgegjinlmbohfolnjikohadamimmmfidfheedf","ldfpomgdngjodbjcaaebgjfmdepb","mnhapgbnkglehifjjilkodmdmcipggncapbmnkcakghdnmbfldlpeeaeogniajbjdpllaaceiknchbkh","pmklpkanghcnmipnfepneel","lbdmebcjikjldkpnnhebfbkcndooellfgpbcdokmgbfedhfggmnhgcdjgmemdpnncedpbkhpaaaaelffgpijdhlhfpiochhggoo","cimcacjahbmpkilfmkjpchpglanphmajmnmjfdnnnemjcbkphjbkmmdbppkljnplballcfcngaannhpioiilldboccjji","eddaplpoceegnemdieneoonkomcfaiejegi","beeoehjdbeokhmcekihnfpjnkenfmhiegfojjcigimpdojengjadmoafkeaghalkalomgp","lbdlphklknldkaifoenibeemibpcpclgmimopmglbehoohnibefe","hdfilacmbeahciihmman","mnfllcmlolejakappanejdinaplieikmppimdfgnbnokdidjmmpknlhdgbdgjjpajemilbfj","jfmianobkafocalipfkdimjoimofblnkl","ecpnoojjgdnkhclocamkeeigdgcpodfjnkkdgfbagjpaojfnglonpdbodibfljgpamhbofnlidfpfnnlfiidncoleknna","cgpidgckgamhpfhjpgaabniaieipmpigcbdljgafeiebnpho","ojhholkmaahdfdhaoeoneakpgngilfnicokjjlpcghgdooghihajgno","mpefgibniimmdpgggimonjmgkhpjgfogbkgpjcgbpinnddpgmhpaf","mhogclefdolmnjehjgidkgkceaofdknlhbjlpdddjcigcbceipjmljdomfghoeebbfodgkdjoghgaopileiijcpblbdjeoaac","ibggmgnojjhgkicknffmhhgnhgmndok","fhpbbkmalfphknckpjpcafopdfhnbjbohcjaifkobahadeoghpenkfaidegpeonaohkofj","hakkhfadibecojfdpcccidcgikfbjconjdgficmphkbe","lhbjoipblfkececccmhifdjabipejoopodnonbgeclfedgmgbkejeigfmadd","icinnjdgfgnhmhfkmpkmilcconldhjkeapglkocplmfjkiaohlebkhloapcodenclomlmlmlgifpcjhedilhohjkpc","mgbmamifhoikehbojnbgcil","ldhkfkajcgocdng","hplolahnkapcohmpbofnpendpndcpeojngeacbmcfmdifdbimkgdoflefeclnjnimdlakcggnkiggiolkllnbl","jlkmhbefoifclponofimafofe","pimpjhclflobnpcfajccajbni","ilpgeefhpldoobmlhmfpocibcmim","gkkfeocokdpoognndfhnhpndcnpj","micgojmfpfnehmlhjaigcegpkbpgikknhdgelfpkpejcdbdfifgdlepimngnoikojijenlm","emcofaadploidipcmalnccnmiegimdigckcimbkonlfanbdljmhgilipmeaeghkbojbiidepcndcammbfkddbiblnjphbk","ljjjeajlonanhgdcfggombfiidpldphlmfhmaalajmdbjine","ojbmmdmoodgedidkbkckjphfcpfkokmflaieiblefjmiafji","djijlldpnnmoppdphcgigoeo","hnjnncfincndoilobppgdbdhnlffhmmbojehocidnffhkhkgmfggaeokeppilk","acehokfnppnooldfogkhbndojfpjchophbodoplebbbhneejanagplhbndfmpeoajipiifeoenhgldl","hj","jfhnfafeopnocgibhohjopmakhaogfhmjcjbhenahpehoddncghdobbcmefnfmjbbidhekklhkpekoch","kboaglapkjmgnjdgafhcbominbajoebgpkfkokbmpdeianecgndhpmcenmhggcegoldmdbcoofhefdaoblidl","nngejbdkjbflghmljpomcbbappefdnlggjjcbhkjchcbhlbkanjinoopilhlcgpmkjpomfocbpkiloogfbcllnjija","nnjnafpdigglkkbcppphechlmgcjleecajpnoaloldjbjkffdibdldndhjdmmhidhopmkopeejpbmdaggakbkmlencoacodckonp","cfpaglkenod","hfebklanpfepbpe","lbmekkahbceggkbmhgeahngkeepjjfnppddageacjkkklnagjmfpbfnkdgiebmalenmopbpjggjkpoaoiflnloeln","ncfgkmmchblfhobhhelpbiogoeamegljmmcpkgnhbkfaiehcofnafbaej","ppmjieodijaaiikmljckmeknagjociabjkfml","ccjoifcnnbeohbjgphomlmpomeignionjlelkccfbhbdpcnmfobihlcomii","lmbjdhkgnboienkgappncgbojinldkiklmaaaffenbbpcdodncombb","madhnihaicigckoldmpmniogjglpakdkpconhomnmlknjnhjcbmcbppglmlppekbamnjbefbkhdaj","epjlohphpecmhhpadfoignomjloaafiamncedlhihodlhdcjpcegedpiebmfbcnofacmhml","lbmhnjjpjgjmaoipffcpimdhelejgfdaaeimajkfjoembjdkikpl","aaikdamdmhkmpcodhbamk","foonflpjdpokgomjdbfegbpchfpkmfg","phkhklhieckkfgodbfaolcppibfmefdhjoficommjcmbccdbidopdjgcodbeemepdakcpbojelhinpobcdciom","plmbogahgldkfffhebbkkelfdoaceloenepimdpadnimfjfemheghnohjonnfbkmngikckbmloejohbbgkpfijjjaldnjah","ogaojibgpjnhhknodibejndfphnmiolikplakjlomjnmnfpigncgccnlcpfjinjidomgcpcfcoceljlmjfmhjkpahhcpiefd","gbiglaopbekamlenjdaplmglagjifinndhklimoloknnjpfpbfglgkfkenkfmbkhgnljfngnmhmhkhcbkamplpmjdb","jaiehenfjnhkbeogefelobcoeklhjffkdeghofekccfpcjgaachkc","oamoffahljpciegohabccooigoojlhdohgdofkldfohoahejgddcfigahe","ebhnhbcdjleaeljpgamnemcljinhhedhlmngeahbpdogkmihdafmdnjnacih","lhkhmkccpggjcbnlgmdinglidbgpfchpfopjabliblceahgkijolmjaldfohnahhllhmnfmlgmobpnmen","gjichlepdcdlaocknmdlgnhnbnmfne","mkjmgibigiobobhcjhcaa","albkcnhbabpecomddgbddkmeinicngjcfoncijpfebmcfjbkemkelelakbnblhpdgjmecbpfaklgnnedpndfcooimj","mbannmpjjbmoefoeojhnhlfbddmhhpgeenmml","iaiigjjaammfbgjdgjejlnhemlceddgclohmnpjceljlpi","bjhhdhndffbaonemgdddnlpmfofld","pokdifalolpeikpdjdnodfjdjfejdlgmllhohaklhnffcijpdenhodddjaealphdpmgbfbbjjnlljbmjleoiclkpefhdjfnnp"]

print maxProduct(sample1)
print maxProduct(sample2)
print maxProduct(sample4)

print doWeShare("a", "aa")


'''



from sets import Set

class Solution(object):
    def doWeShare(self, word1, word2):
        chars = Set()
        for char in word1:
            chars.add(char)
        for char in word2:
            if char in chars:
                return False
        return True

    def maxProduct(self, words):
        wordsLength = len(words)
        tempRes = 0
        for i in range(wordsLength):
            for j in range(i,wordsLength):
                if self.doWeShare(words[i], words[j]):
                    tempRes = max(len(words[i]) * len(words[j]), tempRes)
        return tempRes


'''
