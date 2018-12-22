# Raportti

Miniprojektin tekeminen on sujunut ryhmässämme erittäin hyvin ja olemme ylpeitä lopputuloksesta. Alla yhteenveto projektista.

Ryhmän jäseninä toimivat Dan Lindholm, Philip Ehrnrooth, Simon Nyman, sekä Daniel Riissanen.

## Sprintit

Ensimmäisessä sprintissä pääpaino oli projektin konfiguroinnissa ja sovelluksen rungon luomisessa. Ongelmat, jotka kohtasimme tässä sprintissä liittyivät pitkälti ohjelmistotuotantoprosessiin. Esimerkiksi minkä muotoinen backlogin tulee olla, ja miten siihen lisättäisiin sisältöä järkevästi. Myös käytännönläheisempiä asioita tuli pohdiskeltua, kuten miten merge konflikteista selvitään ilman että ilmestyy ns. merge-helvetti, sekä miten voidaan varmistaa, että tekemämme työ edistyy tasaisesti. Koska ryhmässämme kaikki eivät olleet käyttäneet Djangoa aikaisemmin, niin dokumentaatioon perehtyminen vei osalla huomattavan osan alkuviikkojen työajasta.

Toisessa sprintissä ryhmä oli jo hieman ehtinyt tottua Djangon toiminnallisuuteen. Sprintin aikana toteutettiin muun muassa vinkkien editointi, vinkkien liittäminen käyttäjätiliin ja vinkkien merkkaaminen luetuksi. Työ ei edistynyt ehkä niin tasaisesti kuin olisimme halunneet ja suuri osa toisen sprintin backlogissa olevia stooreja toteutettiin vasta sprintin loppupuoliskossa. Toinen asia, mitä retrospektiivissä mietittiin oli se, että taskeja varattiin sprintin alussa ja toteutettiin/mergettiin vasta myöhemmin. Ongelmaksi koitui se, että jos joku oli tehnyt jonkun taskin valmiiksi, useimmiten ei voinut enää avustaa toisten työtä/lisätä koodia jonkun taskin toteuttamiseen, koska kukaan ei pushannut koodiaan Githubiin, niin että toinen olisi voinut jatkaa siitä, mihin ensimmäinen oli lopettanut, vaan kaikki pushasivat, kun heidän “varaamansa” taski oli valmis. Tämä käytäntö hidasti koodin tuottamista.
Toisen sprintin aikana otimme käytännöksi toistemme koodin katselmoinnin ennen lopullista mergeämistä. Tämä paransi koodin laatua ja oli hyvä tapa vähentää bugien määrää.

Kolmannessa sprintissä yritettiin pitää ryhmächätissä päivittäisiä tilanneraportteja noin yhdeksältä illalla, jolloin jokainen ryhmäläinen kertoi mitä hän oli päivän aikana tehnyt, mitä tulee vielä tekemään, ja mahdollisista vastaan tulleista ongelmista. Alussa käytäntö toimi hyvin, mutta projektin lopussa ei pidetty yhtä paljon tilanneraportoinnista kiinni. Tässä sprintissä yhdellä ryhmäläisistä oli kertausharjoitukset, mikä oli pieni isku meidän devaustahtiin. Selvittiin kuitenkin siitä ja vaaditut toiminnallisuudet saatiin toteutettua. Automaattisten testien kirjoittaminen aloitettiin, vaikkakin pienemmällä skaalalla.

Neljännessä eli viimeisessä sprintissä toteutettiin yksi sovelluksen pääasioita, eli lukuvinkkien ajoittaminen ja kalenteri. Dan löysi sopivan JavaScript-kirjaston ja loi sillä täysin toimivan kalenterin ja lopputulos on varsin miellyttävä. Tässä sprintissä lisäsimme behave-testejä varmistaaksemme että koodi tekee mitä pitääkin. Testejä olisi voinut tehdä enemmän, mutta aikarajoitteista johtuen päädyimme tyytymään olemassa oleviin testeihin, jotka kuitenkin testaavat hyvällä tasolla sovelluksen perustoiminnallisuuksia. Lisäksi tässä sprintissä viimeisteltiin sovelluksen ulkoasu ja viilattiin pois pienehköjä bugeja.

## Kehitysprosessi

Tasaista työnjakoa oli osittain vaikea ylläpitää storyjen vaativuuseroista johtuen. Myös ryhmäläisten muilla kurssiin liittymättömillä velvollisuuksilla oli pieni vaikutus työnjaon ajoittaiseen epätasaisuuteen. Yritimme kuitenkin jakaa user storyt sopivan kokoisiksi taskeiksi, niin että useampi ryhmäläinen voisi yhdessä työskennellä saman user storyn parissa samanaikaisesti. Tämä todettiin ihan toimivaksi ratkaisuksi niissä tapauksissa, joissa kokeiltiin kyseistä menetelmää, vaikkakin jälkeenpäin todettuna oltaisiin voitu harrastaa tätä laajemminkin.

Olisi ollut hauskaa myös oppia jotain Lean-menetelmästä ja miten sitä käytännössä toteutetaan, kun kurssilla oli jonkin verran puhuttu siitä. Ohjelmistosuunnittelua olisi myös ollut mukava oppia enemmän, koska projektissamme käytettiin kutakuinkin valmiiksi luotua rakennetta, johtuen Djangon suositelluista kehitystavoista.

Retrospektiivitekniikkana meillä oli käytössä “Start, stop, continue, more of, less of”-pyörä. Oli ihan hyödyllistä tutustua strukturoidumpiin palautetekniikkoihin. Taisimme kuitenkin näin pienessä ryhmässä suosia enemmin epämuodollista keskustelua, tärkeämmältä tuntui ehkä saada ylipäätään aikaan fyysinen tapaaminen. Sikäli kuin sitä noudatettiin, niin myös päivittäiset tilanneraportit tukivat projektin edistymistä mukavasti. Velvollisuus ilmoittaa joka ilta tekemisistään auttoi aktivoimaan ryhmää ja myös lisäsi ryhmätyön tunnetta, vaikka työtä tehtiin erikseen etänä. 


## Yhteenveto

Yleisesti katsottuna projekti on sujunut tosi hyvin. Ryhmässämme oli hyvä yhteishenki ja kommunikaatio toimi moitteetta. Olemme oppineet miten backlog luodaan ja kuinka sitä ylläpidetään, miten keskustellaan asiakkaan kanssa vaatimuksista ja millä tasolla niitä tulisi tarkentaa, sekä miten toiminnallisuutta tulisi priorisoida. BDD on nyt selkeämpi termi, kun ollaan tehty testausta storyjen tasolla. Teknisellä tasolla ollaan opittu miten Django toimii, ja myös miten käytetään behave-testausta Django-projektissa.


