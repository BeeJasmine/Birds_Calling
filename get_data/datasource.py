import requests
import wget
import re
import sys
#x = sys.path
#print(x)

def get_urls(specie_hyperlink):
    #res = requests.get('https://www.xeno-canto.org/api/2/recordings?query=cnt:france')
    #res = requests.get('https://www.xeno-canto.org/api/2/recordings?query=bearded+bellbird+q:A')
    res = requests.get(specie_hyperlink)
    res = res.json()
    empty_list=[]
    res_list = res.get('recordings')
    for ele in res_list:
        print(ele["file"])
        if ele["file"] != None:
            empty_list.append("https:" + ele["file"])
    return empty_list
    #print(res.get('recordings')[0].get('file'))
    #print(res.get('recordings').get('file'))


# def remove_backslash(empty_list):
#     urls_list = []
#     for url in empty_list:
#         url_regex = re.findall("\/{2}(www.xeno-canto.org\/\d{6}\/download)", url)
#         print(url_regex)
#         urls_list.append(url_regex)
#     return urls_list


def download_mp3(urls_list, path):
    for url in urls_list:
        wget.download(url, path)
        # wget.download(url, '/data/species_name')



#print(get_urls('https://www.xeno-canto.org/api/2/recordings?query=bearded+bellbird+q:A'))
# #print(bellbirds_urls)

#bearded_bellbird_urls = remove_backslash(original_urls)
#print(bearded_bellbird_urls)

# BEARDED BELLBIRDS
#bellbirds_urls = get_urls('https://www.xeno-canto.org/api/2/recordings?query=bearded+bellbird+q:A')
#download_mp3(bellbirds_urls, "bellbird.mp3")
#download_mp3(bellbirds_urls, "data/bearded_bellbird/bearded_bellbird.mp3")

# TRINGA GLAREOLA

#glareola_urls = get_urls("https://www.xeno-canto.org/api/2/recordings?query=tringa+glareola+q:A")
#download_mp3(glareola_urls, "tringa_glareola.mp3")


# Anas Platyrhynchos (Canard colvert)

anas_platyrhynchos_urls = get_urls("https://www.xeno-canto.org/api/2/recordings?query=Anas%20platyrhynchos")
download_mp3(anas_platyrhynchos_urls, "anas_platyrhynchos.mp3")


# Anas zonorhyncha (Canard de Chine)

anas_zonorhyncha_urls = get_urls("https://www.xeno-canto.org/api/2/recordings?query=Anas+zonorhyncha")
download_mp3(anas_zonorhyncha_urls, "anas_zonorhyncha.mp3")

# Anas sparsa (Canard noirâtre)
# 
# 
# Ateryx_Mantelli (Kiwi de Mantell )
ateryx_Mantelli_urls = get_urls("https://www.xeno-canto.org/api/2/recordings?query=Ateryx+Mantelli")
download_mp3(ateryx_Mantelli_urls, "ateryx_mantelli.mp3")




# Perdrix grise	Perdix perdix		243	52 
perdix_perdix_urls=get_urls("https://www.xeno-canto.org/api/2/recordings?query=perdix+perdix")
download_mp3(perdix_perdix_urls, "perdix_perdix.mp3")


# Kilombero Cisticola	Cisticola tax.nov.kilombero_1		91	1
# Tête-de-peluche couronné	Catamblyrhynchus diadema		39	5
# Cici fuligineux	Tiaris fuliginosus		75	16
# Tiaris grand-chanteur	Tiaris olivaceus		114	74
# Cici obscur	Tiaris obscurus		44	20
# Cici verdinère	Tiaris bicolor		56	24
# Sucrier à ventre jaune	Coereba flaveola		502	744
# Sporophile curio	Oryzoborus angolensis		142	52
# Sporophile à ventre blanc	Sporophila leucoptera		58	29
# Sporophile à ventre jaune	Sporophila nigricollis		165	48
# Sporophile bouveron	Sporophila lineola		81	42
# Sporophile noir et blanc	Sporophila luctuosa		72	10
# Sporophile de Morelet	Sporophila morelleti		102	90
# Sporophile corvin	Sporophila corvina		55	26
# Saltator strié	Saltator striatipectus		195	262
# Jacarini noir	Volatinia jacarina		264	338
# Sporophile à front blanc	Sporophila frontalis		94	97
# Sporophile de Temminck	Sporophila falcirostris		81	30
# Saltator à gorge noire	Saltator atricollis		112	22
# Saltator à bec orange	Saltator aurantiirostris		151	222
# Saltator olive	Saltator similis		187	329
# Saltator gris	Saltator coerulescens		388	570
# Saltator ardoisé	Saltator grossus		261	467
# Saltator fuligineux	Saltator fuliginosus		114	92
# Saltator à tête noire	Saltator atriceps		105	75
# Saltator des grands-bois	Saltator maximus		269	390
# Embernagre à cinq couleurs	Embernagra platensis		121	15
# Grand Tardivole	Emberizoides herbicola		127	38
# Sicale bouton-d’or	Sicalis flaveola		212	218
# Sicale des savanes	Sicalis luteola		147	32
# Haplospize unicolore	Haplospiza unicolor		88	57
# Incaspize petit-deuil	Phrygilus fruticeti		86	27
# Araguira rougeâtre	Coryphospingus cucullatus		99	27
# Percefleur masqué	Diglossa cyanea		119	91
# Percefleur à flancs blancs	Diglossa albilatera		116	56
# Tangara guira	Hemithraupis guira		113	72
# Tersine hirondelle	Tersina viridis		81	47
# Calliste septicolore	Tangara chilensis		92	92
# Tangara à dos noir	Pipraeidea melanonota		112	9
# Tangara à poitrine fauve	Dubusia taeniata		112	21
# Tangara de Rieffer	Chlorornis riefferii		82	22
# Tangara à ventre rouge	Anisognathus igniventris		149	56
# Tangara montagnard	Buthraupis montana		91	20
# Tangara des palmiers	Thraupis palmarum		169	181
# Tangara évêque	Thraupis episcopus		186	248
# Tangara sayaca	Thraupis sayaca		125	144
# Tangara à bec d’argent	Ramphocelus carbo		171	375
# Tangara couronné	Tachyphonus coronatus		110	60
# Tangara à tête grise	Eucometis penicillata		99	18
# Tangara à coiffe blanche	Sericossypha albocristata		107	9
# Dickcissel d’Amérique	Spiza americana		175	140
# Évêque indigo	Cyanoloxia glaucocaerulea		18	4
# Évêque bleu-noir	Cyanocompsa cyanoides		132	59
# Évêque de Rothschild	Cyanocompsa rothschildii		119	66
# Évêque de Brisson	Cyanocompsa brissonii		104	16
# Guiraca bleu	Passerina caerulea		194	385
# Passerin indigo	Passerina cyanea		250	436
# Passerin azuré	Passerina amoena		149	141
# Passerin varié	Passerina versicolor		69	118
# Passerin nonpareil	Passerina ciris		102	41
# Cardinal rouge	Cardinalis cardinalis		632	2508
# Cardinal jaune	Pheucticus chrysopeplus		75	337
# Cardinal pyrrhuloxia	Cardinalis sinuatus		101	177
# Cardinal flavert	Caryothraustes canadensis		127	60
# Cardinal à poitrine rose	Pheucticus ludovicianus		172	134
# Cardinal à tête noire	Pheucticus melanocephalus		262	485
# Habia de Stolzmann	Chlorothraupis stolzmanni		105	40
# Habia à gorge rouge	Habia fuscicauda		112	32
# Habia à couronne rouge	Habia rubica		251	164
# Piranga à tête rouge	Piranga ludoviciana		162	465
# Piranga écarlate	Piranga olivacea		170	160
# Piranga vermillon	Piranga rubra		264	212
# Paruline dorée	Myioborus ornatus		109	62
# Paruline à calotte rayée	Basileuterus culicivorus		353	762
# Paruline triligne	Basileuterus tristriatus		188	145
# Paruline du Canada	Cardellina canadensis		171	45
# Paruline à calotte noire	Cardellina pusilla		313	408
# Paruline à ailes blanches	Myioborus pictus		164	175
# Paruline ardoisée	Myioborus miniatus		303	417
# Paruline à calotte rousse	Basileuterus rufifrons		217	84
# Paruline à diadème	Myiothlypis coronata		245	324
# Paruline flavescente	Myiothlypis flaveola		174	143
# Paruline à paupières blanches	Myiothlypis leucoblephara		152	305
# Paruline à cimier noir	Myiothlypis nigrocristata		198	156
# Paruline à croupion fauve	Myiothlypis fulvicauda		214	44
# Paruline des rives	Myiothlypis rivularis		117	29
# Paruline à gorge noire	Setophaga virens		151	232
# Paruline citrine	Myiothlypis luteoviridis		95	42
# Paruline des prés	Setophaga discolor		119	99
# Paruline de Grace	Setophaga graciae		118	172
# Paruline grise	Setophaga nigrescens		162	169
# Paruline de Townsend	Setophaga townsendi		153	88
# Paruline à capuchon	Setophaga citrina		232	176
# Paruline flamboyante	Setophaga ruticilla		355	459
# Paruline tigrée	Setophaga tigrina		93	9
# Paruline azurée	Setophaga cerulea		102	31
# Paruline à collier	Setophaga americana		237	266
# Paruline à joues noires	Setophaga pitiayumi		310	492
# Paruline à tête cendrée	Setophaga magnolia		215	231
# Paruline à poitrine baie	Setophaga castanea		84	17
# Paruline à gorge orangée	Setophaga fusca		177	81
# American Yellow Warbler	Setophaga aestiva		445	1451
# Paruline jaune	Setophaga petechia		160	92
# Paruline à flancs marron	Setophaga pensylvanica		199	186
# Paruline rayée	Setophaga striata		198	126
# Paruline bleue	Setophaga caerulescens		134	106
# Paruline des pins	Setophaga pinus		142	132
# Paruline à croupion jaune	Setophaga coronata		228	398
# Paruline d’Audubon	Setophaga auduboni		178	621
# Paruline masquée	Geothlypis trichas		510	1343
# Paruline voilée	Geothlypis velata		166	44
# Paruline des buissons	Geothlypis tolmiei		249	121
# Paruline triste	Geothlypis philadelphia		169	32
# Paruline du Kentucky	Geothlypis formosa		148	47
# Paruline à ailes dorées	Vermivora chrysoptera		101	22
# Paruline à ailes bleues	Vermivora cyanoptera		136	78
# Paruline noir et blanc	Mniotilta varia		234	188
# Paruline de Swainson	Limnothlypis swainsonii		160	29
# Paruline obscure	Leiothlypis peregrina		207	205
# Paruline verdâtre	Leiothlypis celata		294	288
# Paruline de Lucy	Leiothlypis luciae		96	279
# Paruline à joues grises	Leiothlypis ruficapilla		165	150
# Paruline couronnée	Seiurus aurocapilla		242	444
# Paruline vermivore	Helmitheros vermivorum		123	47
# Paruline hochequeue	Parkesia motacilla		152	30
# Paruline des ruisseaux	Parkesia noveboracensis		296	221
# Carouge guirahuro	Pseudoleistes guirahuro		95	1
# Carouge à calotte rousse	Chrysomus ruficapillus		104	43
# Carouge chopi	Gnorimopsar chopi		142	196
# Carouge à ailes baies	Agelaioides badius		114	33
# Quiscale des marais	Quiscalus major		93	225
# Quiscale à longue queue	Quiscalus mexicanus		263	628
# Quiscale bronzé	Quiscalus quiscula		160	263
# Quiscale chanteur	Dives dives		126	264
# Vacher à tête brune	Molothrus ater		270	507
# Carouge à épaulettes	Agelaius phoeniceus		688	2584
# Vacher criard	Molothrus rufoaxillaris		100	2
# Vacher luisant	Molothrus bonariensis		179	53
# Oriole variable	Icterus pyrrhopterus		111	16
# Oriole masqué	Icterus cucullatus		187	215
# Oriole des vergers	Icterus spurius		167	124
# Oriole de Baltimore	Icterus galbula		231	273
# Oriole de Bullock	Icterus bullockii		220	259
# Oriole à dos rayé	Icterus pustulatus		146	437
# Cassique cul-rouge	Cacicus haemorrhous		164	308
# Oriole jaune-verdâtre	Icterus parisorum		170	202
# Oriole noir et or	Icterus chrysater		164	76
# Cassique à bec blanc	Cacicus leucoramphus		115	29
# Cassique cul-jaune	Cacicus cela		287	510
# Cassique solitaire	Cacicus solitarius		113	38
# Cassique à épaulettes	Cacicus chrysopterus		117	39
# Cassique de Montezuma	Psarocolius montezuma		105	100
# Cassique roussâtre	Psarocolius angustifrons		267	394
# Cassique huppé	Psarocolius decumanus		207	220
# Cassique vert	Psarocolius viridis		114	40



















