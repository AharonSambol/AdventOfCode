HAI 1.2
    CAN HAS STRING? BTW LIBRARY
    HOW IZ I ADVENTpt1 YR INPUT BTW FUNCTION NAMED ADVENTpt1 WHICH TAKES THE STRING "INPUT" AS INPUT
        BTW VARIABLE DECLIRATIONS
        I HAS A COUNT ITZ 0 
        I HAS A LENGTH
        I HAS A PART ITZ 0
        I HAS A MIN ITZ 0
        I HAS A MAX ITZ 0
        I HAS A LOOKINGFOR ITZ A YARN BTW YARN IS STRING
        I HAS A FOUND ITZ 0
        BTW GET LENGTH OF INPUT (WHICH IS A STRING)
        LENGTH R I IZ STRING'Z LEN YR INPUT MKAY 
	    IM IN YR LOOPY UPPIN YR INDX TIL BOTH SAEM INDX AN LENGTH BTW LOOPING OVER ALL THE CHARACTERS IN THE STRING
            I HAS A CHAR ITZ I IZ STRING'Z AT YR INPUT AN YR INDX MKAY BTW GET THE CHAR AT THAT INDEX
            VISIBLE CHAR BTW PRINT CHAR
            CHAR, WTF? BTW SWITCH STATEMENT ON CHAR
                OMG "," BTW CASE CHAR == ","
                    BTW CHECK IF RIGHT NUMBER OF APEARENCES OF CHAR
                    BOTH OF BOTH SAEM  SMALLR OF FOUND AN MAX  AN FOUND    AN    BOTH SAEM  BIGGR OF   FOUND AN MIN  AN FOUND 
                    O RLY? 
                        YA RLY
                            COUNT R SUM OF COUNT AN 1 BTW ADD 1 TO COUNT (COUNT++)
                    OIC
                    BTW RESET ALL VARIABLES
                    PART R 0
                    FOUND R 0
                    MIN R 0
                    MAX R 0
                GTFO
                OMG "-"
                    PART R 1 BTW GOT ONE NUMBER
                GTFO
                OMG ":"
                    PART R 3 BTW GOT BOTH NUMBERS AND CHAR WERE LOOKING FOR
                GTFO
                OMG " "
                    BOTH SAEM PART AN 1
                    O RLY?
                        YA RLY
                            PART R 2 BTW GOT BOTH NUMBERS
                    OIC
                GTFO
                OMGWTF
                    PART, WTF?
                    OMG 0
                        MIN R PRODUKT OF MIN AN 10 BTW MULTIPLY MIN BY 10
                        MIN R SUM OF MIN AN MAEK CHAR A NUMBR BTW CONVERT CHAR TO INT AND THEN ADD IT TO MIN 
                    GTFO
                    OMG 1
                        MAX R PRODUKT OF MAX AN 10 BTW MULTIPLY MAX BY 10
                        MAX R SUM OF MAX AN MAEK CHAR A NUMBR BTW CONVERT CHAR TO INT AND THEN ADD IT TO MAX 
                    GTFO
                    OMG 2
                        LOOKINGFOR R CHAR BTW LOOKINGFOR=CHAR
                    GTFO
                    OMG 3
                        BOTH SAEM CHAR AN LOOKINGFOR BTW IF CHAR==LOOKINGFOR
                        O RLY?
                            YA RLY
                                FOUND R SUM OF FOUND AN 1 BTW FOUND++
                        OIC
                    OIC
                OIC
        IM OUTTA YR LOOPY
        BTW CHECK IF LAST NUM FILLS CRITERIA (I DONT NEED THIS I CAN PUT , AT END OF INPUT)
        BOTH OF BOTH SAEM  SMALLR OF FOUND AN MAX  AN FOUND    AN    BOTH SAEM  BIGGR OF FOUND AN MIN  AN FOUND
        O RLY?
            YA RLY
                COUNT R SUM OF COUNT AN 1
        OIC
        VISIBLE "WAHOO" BTW PRINT
        VISIBLE COUNT BTW PRINT
    IF U SAY SO BTW END FUNCTION



    HOW IZ I ADVENTpt2 YR INPUT BTW FUNCTION NAMED ADVENTpt2 WHICH TAKES THE STRING "INPUT" AS INPUT
        BTW VARIABLE DECLIRATIONS
        I HAS A COUNT ITZ 0
        I HAS A LENGTH
        I HAS A PART ITZ 0
        I HAS A MIN ITZ 0
        I HAS A MAX ITZ 0
        I HAS A LOOKINGFOR ITZ A YARNBTW YARN IS STRING
        I HAS A FOUND ITZ 0
        BTW GET LENGTH OF INPUT (WHICH IS A STRING)
        LENGTH R I IZ STRING'Z LEN YR INPUT MKAY 
        BTW LOOPING OVER ALL THE CHARACTERS IN THE STRING
	    IM IN YR LOOPY UPPIN YR INDX TIL BOTH SAEM INDX AN LENGTH 
            BTW GET THE CHAR AT THAT INDEX
            I HAS A CHAR ITZ I IZ STRING'Z AT YR INPUT AN YR INDX MKAY 
            VISIBLE CHAR BTW PRINT CHAR
            CHAR, WTF? BTW SWITCH STATEMENT ON CHAR
                OMG "-"
                    PART R 1 BTW GOT ONE NUMBER
                GTFO
                OMG ":"
                   PART R -1 BTW GOT BOTH NUMBERS AND CHAR WERE LOOKING FOR
                   BTW CHECK IF THSE INDEXES ARE GOOD AND THEN SKIP TO ,
               
                    I HAS A FIRST ITZ I IZ STRING'Z AT YR INPUT AN YR SUM OF INDX AN SUM OF MIN AN 1 MKAY
                    I HAS A SECOND ITZ I IZ STRING'Z AT YR INPUT AN YR SUM OF INDX AN SUM OF MAX AN 1 MKAY
                    BOTH OF    DIFFRINT FIRST AN SECOND     AN      EITHER OF BOTH SAEM FIRST AN LOOKINGFOR AN BOTH SAEM SECOND AN LOOKINGFOR
                    O RLY?
                        YA RLY
                            COUNT R SUM OF COUNT AN 1
                    OIC
                    BTW RESET ALL
                    PART R 0
                    FOUND R 0
                    MIN R 0
                    MAX R 0
                GTFO
                OMG " "
                BOTH SAEM PART AN 1
                O RLY?
                    YA RLY
                        PART R 2 BTW GOT BOTH NUMBERS
                OIC
                GTFO
                OMGWTF
                    PART, WTF?
                        OMG 0
                            MIN R PRODUKT OF MIN AN 10
                            MIN R SUM OF MIN AN MAEK CHAR A NUMBR
                    GTFO
                    OMG 1
                        MAX R PRODUKT OF MAX AN 10
                        MAX R SUM OF MAX AN MAEK CHAR A NUMBR
                    GTFO
                    OMG 2
                        LOOKINGFOR R CHAR
                    GTFO
                OIC
            OIC
        IM OUTTA YR LOOPY
        VISIBLE "WAHOO"
        VISIBLE COUNT
     IF U SAY SO



    I HAS A INPUT ITZ "4-8 g: ggtxgtgbg,13-14 q: qmzdrtqctvrqsb,1-5 d: ddddlddzfdd,1-3 f: pfhff,4-5 c: ccssnccccc,5-6 l: lzlwll,6-8 v: vvwhzpxvvv,1-11 h: scschhrqhpc,12-15 t: ltmcbztvttgljtr,5-12 h: vcvvhnjhdllhlbzk,11-16 j: jjjjjjjjjjjjjgjjjj,2-4 k: vkzk,9-13 c: bcbkccccpcchd,6-7 n: nnnfjnn,4-9 z: lztmfrqqz,1-3 q: nqlqdbc,1-11 v: jvvvvvvvvvvvvvvvvvvv,1-3 m: mqmzm,1-4 c: cccccc,3-9 b: bblbbbbbxbbbbbbhb,1-4 q: qqpkkfkmldl,4-5 q: qqqlqq,3-7 h: hhchhhghhhhh,1-11 l: qllcvlbsllsllllllll,2-4 d: bdkd,4-5 x: bqnpd,5-14 z: vcmggppvzmzwkn,2-4 p: ppppp,3-4 f: jffm,8-19 b: blbfbbxxtszvpfwbrgd,13-17 v: vvvvvvvvvvvvvvvvvvv,6-15 f: fftfftfffpfffvl,5-7 v: tmvgvnv,2-6 n: dblnvmhkqsctbt,4-11 j: bsljpqblsjjffqshq,7-11 w: hwlwwwqwcwrwwwww,3-4 k: hkwj,8-14 m: mmmmmmmqmmmmmqm,4-8 f: fckfxpmb,2-3 b: dbbvbrbhb,10-14 t: ktmtfmttmrtlmdttt,7-10 k: khkkkmkqhkx,1-5 n: cwmtx,1-4 s: ssssnngps,3-5 m: pxmmkqmrhjm,4-16 t: xlbtptqdbnrlpnwttlz,1-17 h: hhhhshhhhhhhhhhhwhhh,4-10 h: dvhtpfrxch,2-13 r: ljcsxtrzqmkwn,1-6 w: xpnzqdwwdww,5-9 d: ddddddddddd,2-10 d: ddddddddddddddd,6-8 d: mdnmdddddz,8-12 k: kbkrzcqzrnxf,3-4 m: kctqmwm,1-4 w: wwbw,3-4 t: zfzt,7-9 x: xxxxxcxxvxx,7-11 v: vvvvvvvvvvvvv,1-3 r: rrrj,6-8 x: tpkxpcdxbvhsd,6-10 b: cdnkjbqzzbjrbbtgkn,5-10 z: zzzzfzzzzz,2-13 s: rqfbzzmjxmjbvm,5-6 f: lfffsm,1-2 n: nqnn,1-4 d: hddt,3-4 p: vpqpmbppsbct,4-9 k: jcqsdmlpvk,18-19 q: qqqsqbqzzhqqwtqqqlmq,4-10 s: sshssssscssws,11-17 v: vvttvgvvvvvvntvvvvv,2-3 t: jtttggtsbct,4-18 k: vkktttwkjkkkjkvgkkk,2-12 h: xhdcktkhnqvh,1-11 m: mmlmmmmmmmm,8-9 w: ntwwwbwwwsldnwwwwvjs,4-7 s: sdwshqskhc,3-11 q: qqvqqqxcqqvq,9-10 k: ckgkbkfkkk,1-5 s: sssjssssrsssk,12-16 t: tttttmttttttttttttt,6-7 b: bbbbbbjzb,3-5 m: mmwmzm,3-4 q: qqqq,2-8 h: hhhhhhhhh,5-9 t: jsvtnzfrtptwh,6-7 q: qvqqqdbq,10-12 t: tttdttmtttttttt,8-10 b: grbbbbbbft,17-18 p: ppppppppppppxppppp,10-11 c: ccccccccccjcccccccc,4-5 h: hhhhhhhhhhhhhhthlhh,5-11 z: zzzfzqjzzlzzzzzzzzz,4-6 f: fhhtfd,5-7 w: wnxgzsj,2-6 b: lbbdjb,12-15 v: ngvkpbjqbnhkvvhwn,4-5 v: vvvxr,8-16 t: clwmtjgttpwttsttdn,1-4 z: kzzz,8-11 c: wccdpfhctfvmb,4-7 z: xzjzvqqzr,10-13 g: hgwgggrggxgwgggg,2-4 q: kqwqjq,3-10 m: rmdjwnjpfqshm,6-7 n: nsnnwnnzlfzdnxfn,2-5 f: pgfhc,17-19 z: jzzzzvcbfzlzzszpbwx,5-9 w: pwgtwldswqtgrcw,4-11 w: wwwwwwwwwwwwwwww,4-5 c: lccrf,1-3 s: msfsl,3-6 m: mmmfmmmmmmm,13-14 b: dzbwccbbtxbbbb,13-14 g: ggghgpgggnggncgggc,1-4 q: rqqhq,1-4 p: pbpp,2-17 z: zzzzvzzzzzzzzzzzzzz,7-12 m: mmtlhmmlmrzfmmmmfvq,4-7 v: vvvlvvxvvdv,10-12 x: xkqxbtxkxjtgq,2-5 v: gchvk,5-6 l: jgcltxfvvwlv,2-4 w: rwrdstmwrppxks,2-3 l: kspmt,10-12 n: nnpnnnnnnnnnnn,6-8 l: lbllljlw,3-4 b: qnbp,7-8 h: hmkvkshh,8-9 r: rrkrwrrzt,4-10 g: rggggzzshg,1-2 x: rfxxxjxxx,11-12 l: qlzltcllllllx,2-10 b: bbbxqttmnbxbbxdbhv,2-7 k: fkvfrmkpcb,8-9 z: zjswlzbdprzzzhzfdkz,1-8 z: zzzkzzgz,6-8 s: stssjsssbsvss,7-12 g: gggdgphgcggrgggdg,10-16 v: thbdxcpmvrrwdcglzlf,6-9 q: qqqqqqqqqq,6-8 w: rvxwfsxshwxn,5-6 f: ffffff,16-17 z: zwdzczzzzgznjszsx,8-14 g: wlvxzjcndbgmgt,3-7 k: kzkgtfk,13-14 z: jxzjgmdzvjssknjc,10-12 f: fffbfjfhmflf,13-15 j: jjjjjdjdbjjkjjj,2-3 d: cddddfrg,14-15 v: vlqvvcnjzvvvlvv,2-4 r: wrrh,14-16 p: pppppppppppppppkp,13-19 p: frphddzlxckwccpgphh,6-7 l: llrdllh,2-3 n: wnswnq,7-8 s: sscssssss,9-10 r: rrxrxrmrrr,12-15 q: fqqqqjqkqqqqqqq,2-6 n: hlnkfv,8-10 f: fffffffffsf,6-7 d: bndhfwhk,4-5 p: fnkjn,6-9 f: fsnfswlpx,7-8 d: bpqcsmdqkndndldx,4-6 n: jndndnlwl,15-16 k: kkkxknpckkjktkjkkk,3-10 b: bbrbrbbbbtggbbb,10-17 t: tttttttbtqttttttttt,6-8 l: xfplllll,6-7 f: tfjjwjfrfmhtvlq,12-13 q: qsqknjpfxrdmj,10-17 b: gbzmbbtrvblbdmbnbznv,5-10 f: hsfbrfffffxnffmnff,4-5 q: rqqzq,12-13 m: mmnmcgwwmdsmmm,1-10 f: nrfmffsfrdfsdfrbf,1-2 p: ppppx,15-16 c: sdvfscmzgcpvtbhc,1-2 g: xfggggg,14-15 n: nkfvtnnfnfdhvnnrnm,10-12 c: ccccccccczscczcc,12-15 q: xbqnbqlbdzqqqqs,6-7 m: mgwmmmrbsmp,1-10 x: xxkxxxxxxxxxx,4-6 j: jjqmcc,6-8 b: bbbbvbbzbbb,7-12 m: mgmmmmtmmmmh,7-12 p: pdpplppppxzp,5-9 d: tdwddnkqx,1-4 r: drrv,3-8 w: wwrwwwwmwww,7-8 b: bvbbbbjxhb,8-13 p: pppbpmpppznsppj,2-4 l: tjlhlcjsgvsv,2-4 p: pppjfkbn,3-9 r: jnghndjrrrfrchrjnrh,2-3 d: dlzwbj,1-7 g: xgwvggtgggv,9-17 t: xmxdvthxtwwcbvplt,6-9 h: hhhhhvzhk,2-4 l: vljljlf,8-9 l: llltblllll,6-9 w: sfzzlrsbmtqlzds,8-11 b: bbbbhbblbbqbmbw,2-4 s: ssss,16-18 k: kkkkkkkkkkkkkkkpkfk,5-11 f: xppmqnnfzgrlfjfffmd,6-12 b: bzzbhbvgkxrb,3-7 l: hftlxwl,5-11 k: kkckftpsjxvv,7-11 h: hhhhhhrhhhhh,10-11 v: vvvvvzvvvvvvvvvv,2-8 k: pkmwlnkk,14-17 v: vpvvlvrwvvvkvvwvvvv,2-3 v: vkbw,1-7 z: mzzzpzsrrszzzzw,5-6 k: kqckkb,3-9 q: tvdjmqwhqhfqv,3-5 f: ftkff,18-19 t: ftttsvvvztbgrsrzxsrg,3-5 w: jkgwwbc,6-7 d: dvwvddf,3-4 k: mkkk,6-10 h: cjhkhhghjlhhh,4-8 r: grbrrrhrrtrrrlbdvq,6-10 r: frrlrrrrmrrrrrqr,3-4 f: rnftfffdfljqtgffvck,4-6 j: jcvjjjljj,9-10 m: sztmdqxdrlfr,2-5 s: pdssgsss,3-5 h: sqhdhcdhhx,3-7 c: mccnccvkccn,5-11 n: nnnnwnnnnnbn,15-16 d: ddddddddddhdddxzdd,9-10 d: ddddddddddd,13-16 l: twgnssbrlljflgnl,6-12 n: nnnnnnnnnjnnnn,5-9 z: zzzznzlznczzzzjlzz,3-6 v: vvvvjvv,3-7 w: lwwtxdwhxncnv,8-16 n: csnbmrtpdfjfjfxrvz,1-9 m: mmmmmmmmmmmhmm,17-19 h: hhhhhphhhhmvchlhtgt,1-8 t: ttttttttttttt,9-18 j: djjjfpjdjfjjjdmxlj,1-8 d: mddmdddddddddddddd,6-9 c: mnpcwljnc,12-14 m: mmmmmmmmmmmmmq,15-18 j: nzztskzkgxjfdljnchm,13-16 z: zzzpzzzzzztzwzzbzz,3-4 s: cskxxssswzn,3-19 n: nnknncnnnnnznnbjnnn,12-15 w: fcwvgwjwgmlwwwj,11-17 q: bzlbnrsqgkqkqqpdj,4-13 j: kcjjgwjjkzwrj,4-6 k: zdskmkzxhksjrdhqnm,2-9 b: bbbbbbbbbbbkbbbbbbmh,5-7 v: vvvvvvbv,1-7 z: tzzzznvzz,2-3 l: llllv,3-15 w: wwrpcwwblcxwwsbjww,1-2 x: hxtntlprztgxrtw,3-9 z: zzzlzzzznzzh,9-10 c: clccsjcccc,3-4 r: wfrr,10-13 c: dchccccccwccfc,15-16 j: jjjjjjjjjjljjjzfjj,3-11 k: sdtqsrlzdcpwgwz,3-4 t: tskl,3-4 m: bxpc,7-12 n: pnjxqssqxndcxdh,14-17 g: qhkwgpgdgzgfgsglvggb,2-3 s: ssss,12-18 f: bszfnfjkwlmfqkfjgf,7-12 p: hzlppppmpwppsswdmxcq,4-5 r: rrrtrr,8-9 b: bbzbbgbgbbtbbbb,9-10 w: fwxkvlwhchqsvmqpcvjk,5-8 x: xxfxxxxxlxgxxxxxxxx,15-17 p: pppptbpxpppppmpspp,3-4 p: ppflppppppp,8-12 h: vvddrhxjrnnwq,5-10 h: hhhhhhhhhhhh,4-15 p: pppdppppppppppvppp,2-3 d: rlwd,13-14 s: pslshszqtszssss,2-3 n: nwwnn,2-10 g: kgggggggggggggk,3-14 j: jgjsjpxjjjjjjjjjjj,13-15 l: lllllllllllllllll,4-7 g: ggggggqgg,4-6 k: vzpkmqqdhbwp,17-18 t: lfmmmzlsppqnfhlltj,3-8 z: jzbspfnrkd,10-16 d: dddddddddddddddddd,4-6 s: ssqsss,1-11 n: znnnnnnnnnvrnlnnnn,9-10 h: hhhhhkhhhzhw,6-9 x: tsxgxgqckxtg,8-14 s: sssssssssrksss,4-5 t: tttsshtt,10-11 j: mlhqgfgdjjjrdvwtx,2-10 l: wlmksskvbl,4-7 v: vvvrvvkv,2-4 f: kfbfn,13-14 z: zqlkpwzrrzpzpz,17-19 d: mcdlxzdcdmvkpdsxdtx,6-9 w: wbczwwhwcwbwww,4-5 h: rrdth,5-6 g: hggvjbhgggggpg,7-16 n: nnfnwmnnnnnnnnng,4-5 v: wckvv,10-15 p: hgbjppplppppkpp,4-6 m: mmmmmmm,11-15 k: kkkkkkkkckmkkkrkkk,7-10 n: nnnnnnvnnnn,7-10 v: rhvpmvvlpvsvv,1-4 g: glgl,6-15 g: jwnggdftwtsmgvg,14-16 h: fdrhhhhzmhgwrhwh,2-3 c: lqfc,16-17 h: hhhhhhhhhhhhhhhhhh,12-18 w: wwwwwgwwwwwwwwwwwwww,5-9 z: rzzjzzzpzzzztnznvxzz,8-9 g: qbgjggmtg,1-4 s: bsscssfssss,2-18 h: btvhfcldlfpgtkrtlh,8-9 b: btgbtdqscw,9-13 x: sxjxxrxxhxnxmx,1-2 w: hffcbd,6-10 g: ggvlmgrgfqgbsbgmg,4-11 m: mmmqmmmmmmmmm,8-10 x: bxrkxxxxxxxx,2-6 q: xgmwbdhptmrxlkrhqwtv,2-3 g: lgpg,7-16 f: kgzdkblmgppfvmkzhdw,12-16 b: bbbbwbbbbbbxbbbbbbb,10-19 m: mmjvhjmmmmrnlfbwbmm,4-5 l: sgzlltmzlrcp,1-13 w: wwwwwwwwwwwwxwwwwwww,2-4 h: whhz,9-13 k: kkfklkkkrkkktk,12-13 p: skplpppdpcpppc,12-14 b: sspbzrsbrdwbcb,2-6 d: bwwhkqrb,2-3 v: vvvgqhv,6-14 b: bbbbbhbbbbbbbkbbb,13-14 n: nnnnnnnnnnnnhqnn,16-17 g: ggwgwngbrxjfhgtdk,4-6 g: nqgrgggggggtggg,2-3 c: cccc,9-15 b: bbwcbxbgcbbbbbh,4-9 s: rsvvssssdssss,1-2 c: cvcg,3-6 l: lfgllllllld,13-14 w: wwwwwwwwwwwwsw,9-19 q: jbmwhjhgqpfqqprdhgm,8-11 b: zbbbbbbmbbvbnbb,6-14 w: wqjkbdmbxktxgwhw,7-9 q: pcphqqswz,4-5 j: jjjjjj,8-11 q: djnqvqcqqxqq,8-9 q: qlqqqqqqv,2-4 k: ltkk,7-11 n: xnlxbqnwbznqbkgl,1-6 q: rjqhtq,4-5 m: mnmhv,4-15 n: thxqsnkkjqfzqjt,4-6 l: qrmlhpsl,4-5 t: tkrvt,1-9 c: ccccccccpc,9-16 h: hbhhjhhhxhhhhhhmh,8-11 r: rrvbvrrbrrl,8-10 c: cpnhccctggc,5-7 r: rrrrhrrr,1-12 v: vvvvvvvvvvvsv,3-6 p: chlbfxmtmpd,5-7 c: cccccccc,6-11 n: nnwnnjnnnnnnnnnnnnn,3-5 r: pfrrj,1-8 v: vpvvvvvvvvvkvvv,14-16 s: ssssssssssssspsqss,9-12 s: hbsjlxgsrcqds,2-16 t: ttttttttttttttct,12-13 t: fshgdtvfbwgtj,9-13 s: ssssssssmsssks,13-14 h: hhhhshhhhhhhhs,1-5 x: jxrxcxxxxx,11-12 f: ffffffffffvfwfff,2-17 w: wpwwwwwwwwwwwwwwk,8-15 g: gggggggqgggggggg,8-14 d: ddldddddpdgddpd,11-16 w: wwwcwtfwwwfwcwbd,1-3 w: wwww,7-9 q: sbpvlqqwqktk,3-5 m: mmpmmmm,2-5 w: kkxwpzgfdtpqkx,2-12 t: vtqpzctjtktttcvp,3-6 b: bsbhpb,2-4 r: jrtcrcrsrs,3-4 c: crcc,1-3 c: cccsc,11-12 q: cxnmpdqbjtqqhqqzq,8-9 v: whvrpxjgjvfv,4-13 c: djqcrmnlkrjfcwcc,4-5 h: cnhnj,8-10 g: tpcgkpmgzg,3-7 w: wvwwwcwwwwww,7-9 z: zcbqfwnhfcw,1-4 v: vvvvvbvvvkvcvv,7-8 x: xxxxxxtg,1-3 p: zpnp,6-8 j: zsjjtwndw,8-9 q: qqqqqqqqqqq,5-7 p: psppphj,4-10 k: vskzkmkqkjz,10-12 p: ppppprppmpppw,5-7 h: hhcmngshnkh,2-3 f: wffjjshgdrdcfpwlz,3-5 z: zzzzz,1-3 p: npsp,10-13 t: thttttjbtpttzt,12-14 h: xmhnhzhzshhhwh,2-10 m: dxfzmxtfrzplpd,7-18 k: vbkkkbgzknljkrkmnn,1-2 n: vknnnnnnnt,9-10 g: gggggggggggg,5-9 t: tttzjttvgttftqttwtfb,7-8 b: bbbbbbbmb,3-4 v: vfvvv,2-4 p: rptpfb,3-4 v: qjns,1-2 w: vtww,8-9 k: kkkkkkskskkkkk,16-18 q: qqqqqqqqqqqqqqqmqqq,2-5 f: kfrff,11-13 h: hhhhhhhhhhhhhh,2-14 l: kgcpljwsxxnzjl,9-11 k: kkkkkkkkkkh,5-6 v: gfvtkf,4-13 n: znnnnsnxzngdntvh,12-16 h: vhhnhhhhphhhhhhhh,6-8 z: wzpztztzz,2-6 s: wnbhsb,1-4 j: jjxj,5-12 t: ttttttttttttt,15-19 r: rrrrrrrrrrrrrrlrrrrr,6-7 k: kpknvdkkkq,1-8 v: gvlvsvvkvd,5-10 k: kkkpkkkzkkkkkkk,4-9 k: kkkskkkkqkkkkk,4-5 p: stcpppk,2-5 q: dwgqf,4-9 l: ccclfrdlccjhjdckwdp,1-3 r: rrvr,4-9 b: bsbdbbbbbbbbb,1-2 t: tltx,13-16 c: ccjjdrptzckcccjc,2-14 b: bbscgbbggprprbjbfbfk,1-3 n: vnvnln,6-7 q: xhqpnxq,1-2 z: mzzzzz,1-11 l: xsqwvlsllllllnhht,3-8 g: ggkggggsg,6-9 m: pzkmmbmmnmhtmmmm,2-7 v: vvvqhlxqlxh,4-5 p: jtpfz,6-7 r: rrrrrhwrr,6-7 p: dtscbppzpz,15-17 x: fkbhvxvkdxxrpgzgvxx,5-6 j: jzjcpf,8-11 n: tnhnvjnnntnzsnn,6-8 j: zjjjmvjnjrjk,1-4 d: dddd,1-2 t: ttjm,9-12 g: fvgbkgmggbzg,2-3 g: nhfdxrcdzxpmqzgmpb,3-4 z: wzrrnr,10-17 j: jjjjjjjjjljjjfjjrj,3-6 j: zjndjqjv,19-20 f: bfgzfsfhxvftfvcrffbf,15-18 z: zzzzzzzzzzzzzzjzzqzz,4-5 w: wjqgf,2-5 t: xtkst,3-6 f: fftffffff,12-13 v: vvrfvvvxvvcvvvj,8-9 c: cccsccccdwcc,10-14 z: cdbzfmpzzmzzzzszzzzz,6-8 d: rddtdddtdj,9-18 m: kpqtmtbxmmfzmhtrfm,3-4 p: zhppjpvl,3-9 m: dmqctlfzmz,7-8 n: nqnnnnnn,9-19 d: djhlrtkdddgzrdqvpfd,10-11 m: qzmmmzmmmmmmmmm,5-7 q: twbnqxqqtksvqqs,4-5 l: cljfjqhqtnrfpm,14-17 k: kkkkkkkkkqkkkkkkkp,10-12 q: rqqqqqgqqjqh,17-19 k: kkkkkkkkkkkkkkkkkkkk,4-5 d: dsdmg,9-15 b: bpsnhlbbbwgbbbbb,2-8 j: wjvjwwbjh,4-5 t: ljxcttv,4-8 p: cbgpnbpgvw,3-4 j: snjf,8-13 t: vtkfttjhtxcfzdm,1-4 h: hhzh,1-15 w: wsltqwxnwwbpbbwfxh,1-16 l: lllllllllllllrlsllll,15-16 t: hhfttcvtvxttjtttt,3-4 k: nkjwkkkkkvk,2-3 h: vshbhh,5-11 r: crrxrrrrrrp,6-7 l: llllbrvtzwlxlr,3-5 z: zhzkz,3-4 j: jmktj,6-8 q: mrdftjqbz,3-4 f: fffff,3-6 z: wmzzztsf,4-5 x: gxlxxxxx,9-12 c: vcggnccqtpccdmvcbz,6-7 l: rgmllktln,2-3 p: pppqpppgvpm,4-9 b: bbbgbhnjbcwqlb,5-6 f: mdngff,8-9 h: hhhhjzrtnbhhhh,11-13 d: cpvddddhdrdvdl,2-4 t: tpxrtpm,14-16 f: wmfffffffbftggftf,6-13 b: bbhjbsblbbbbbtcbbbb,4-5 j: vqjjdjfw,12-14 n: wnnnnrnnngnbnbnnnd,1-12 c: ccccccccccccc,4-7 k: kkjmklfkkkjjkkktkh,4-5 s: sssgx,2-9 r: srvmpjvzrzzncsspftl,4-5 d: ddtgk,6-7 r: zwgwxrz,16-17 m: gxmmmmmmmwmmmmmmmmt,4-10 p: xrrpjcgfwqcwpz,5-6 l: lrlwlp,3-7 x: xmwxxxxsxxxlnhrxx,2-4 g: gmdb,5-9 j: jcrdvkzqp,1-5 z: tzzzkzzz,5-6 b: ljbxbbln,9-10 r: cjrlqctbwgxfshvhr,6-9 r: rlxmrhnrlf,1-6 g: hggggsg,8-14 n: nnnnnnnnnnnnnvnn,7-8 q: fjqrjdqqfqqq,3-10 t: tthttttttjtt,4-8 w: pnjwwmwwwdwwww,2-7 r: rjrrrrr,13-14 q: qcqxqqqcqqfjqqqbqqq,10-13 h: hhhhhhhhhchhkhh,8-9 w: wqkqpwkwwwwbwzwsdnxh,12-16 t: tsrtvgntttwcttrtt,3-8 l: dgfcdlfcg,8-10 p: pppppppckh,11-13 l: lllzlllllljll,3-4 g: ggtgg,4-10 d: vqddddtdtd,15-16 b: bbgbbblcbbbbbbbbb,11-15 l: lljlpllllllwlltllrl,16-17 t: ttttbbmbqtttttvtttt,2-5 r: xfhjb,13-14 c: nmcsccczzbcckccccd,9-10 r: rrrrrrrrrr,1-6 s: ssssssss,11-12 l: lthqbqxjxcll,7-8 j: xrdjjjsv,9-11 s: dsdvmqslsxsshtgdns,7-10 k: rkkkkkskkqxkkk,12-16 q: qqqqqqqqqqqqqqqqq,7-10 z: zzzzzzzzzzzz,3-5 h: nwgbxhfhjhcqw,3-6 x: xckbds,4-7 n: skpwsxq,4-12 j: fcghgztnjbkfcj,7-8 l: ldllngjl,3-6 h: vbqmgpn,4-7 w: wlvnvwwcgbwqdbsd,2-3 l: fllll,1-4 c: gvxn,11-12 n: nnnnnnnnnnnnn,1-5 f: hkffqfffff,4-5 w: wlwwwwwww,12-14 c: cgckcclcnccpch,6-7 g: gwtpfgw,3-4 g: gnddb,5-8 k: ktkkxkkn,8-9 z: zzbbzzzzzzz,2-6 k: fldmgh,2-4 b: llbhbm,2-6 v: vvlvvvvvcvz,14-19 c: sxnckwfhzzcpdcsppbcs,5-7 r: btlsrgrbrjvmlzqhfsz,3-6 q: qqjqqflqf,4-6 j: jjjcjxjj,3-13 x: xxcxxxxxxxxxxxxx,1-3 h: lnvhhz,2-11 f: mcssggwftgb,13-14 w: gznzwwvwlwgdrf,1-2 b: pbbbz,3-11 q: qqqqqqqqqqqzqq,4-6 x: qxvxsg,1-14 r: hrmrrrrrrrrrrzrr,15-16 d: djddqkdfdsdwdgddgd,3-5 q: ljqhqqf,2-4 w: wcwn,4-5 z: zzfzpztcnv,3-6 r: jprrtrq,7-15 t: tttttlttbtttttsttst,2-4 f: fffff,7-8 m: mnmmmmmm,5-7 h: zfhshhh,13-14 s: ssssssscsssssss,5-6 r: rnrrrrcr,13-18 q: tmhkdntqsqqqqpqqhg,11-12 q: qpqqqqhqfqqqr,4-5 l: lkljtnpgvrfgwcmkj,6-12 g: wwmggggjgpggg,9-15 k: xkpckkkjkdkkrkkkkk,7-14 c: bgqcsjcvbggjcxcskr,2-4 s: jsvswj,5-6 k: kkmkshkkk,3-4 p: tkcr,7-8 m: mkmmmfwt,4-5 n: vhndnqjvz,15-16 s: rpczrpjvtssqjfqx,6-8 l: dgmplllfz,7-12 t: ftmttktrttqt,9-17 p: bgxzfjgxprwbhptstvw,3-8 z: zzzzzzzmzzzzzzzz,9-12 x: qngvwfmcxbsxhmx,8-10 s: ssssssnsss,5-7 l: lllllcl,3-4 w: wwnmwwswwww,3-5 m: nsmzmbk,11-12 n: nwbtnnnwndnnnnglnggn,10-14 t: ljdwztvkhtqtfth,1-5 c: vsqhk,3-4 l: vnll,9-19 r: rhfkhcgqmrnrrrlssgz,4-9 z: zzpzzzzzxxzzzz,1-3 x: xxxxx,9-12 k: kkkkkkkkkkkkkk,3-4 v: vvvbv,13-17 p: tpppppppppdpppppppp,10-13 z: zzzzzzzzztzzjz,3-14 m: mqwwhttdksfzwcd,5-6 c: vcccncs,4-5 n: nnbnf,8-17 f: ffffffffffffffffcf,4-7 g: ggghgfvgggg,4-9 p: ppppppppppp,5-7 s: tcsnksgstssqsnns,8-9 q: bqbttzhqrx,13-14 z: zzzzzzhzzzzzzc,1-4 g: gggsg,12-20 j: lqnjfwqlxbnjjmrxvfcz,5-16 c: ccccsccccccccccvc,10-11 h: zhhssmnhhlj,9-12 w: hwwwswcbwwtqlww,9-11 n: nnhnnnnnnjsn,4-5 w: wqngb,2-3 t: tfbtt,9-11 r: rlrrrxlrsrx,8-9 c: ccccccbcc,4-12 j: djgfbvcjrdjhwc,5-7 n: nnknnnknnln,3-6 b: hzbtdb,3-9 w: wwjxlwwvtxwgf,8-17 f: ffcqmzbkrlqpkjkdbsd,8-9 f: ptbdlfvflqh,2-7 v: vvvvdvfdz,3-4 h: hhdhhh,1-8 s: sxngsvsssbsspptjc,4-13 l: lxgspntcmrbplmtq,9-14 f: gffffffffzfffffffff,9-10 r: rrdrrrrrrrr,11-12 k: kkkkbkkkkkkgk,4-5 k: bfgkw,15-17 j: jddrhztkkqjjjljhjjsc,17-18 q: qqfqqrqqqwqqqqqqqtq,7-8 z: zqbzzzdjtzhzxqmkmcvq,6-7 f: xfkrwffncjffj,8-10 q: qqqqqqqqqqq,8-9 s: qwcswlzss,10-11 p: mpppprppspppv,5-18 l: vntgdbclplhklqlqllt,10-11 l: lljlllllllll,6-9 d: dmpdddthjqmcktnf,1-4 m: mmmmmd,6-7 l: lxlllbnl,14-15 s: fssssssssvssssssss,9-13 k: kgkhkkkhkkkkkkkkc,2-12 l: lzlllvlllslwl,18-19 q: gqtqqqqqsqqzqqqzmkm,7-11 l: lllblllllll,15-17 r: qmbrwmlrplrqrrhrzmr,12-20 h: wqmwvfbggczhcrhgkqjw,3-4 s: ssjts,6-11 d: wdtddnddddjdmd,5-6 x: xxxxhx,13-16 j: jzsjjjjjjfjjljqjjj,9-11 p: pppppppppppp,10-13 m: hmmwhkrsvmjmzld,1-2 p: ppppqpskppppk,13-14 x: xvtxxgfpqxfsblxxx,2-3 d: xdgbfpskmlgnmdgv,5-8 s: dwmgtddxgnsqqkvcplgg,1-19 f: fffffqfnfcqfhgffffz,3-6 g: ggdbghggtgggggggndgg,13-18 x: qxgxxxxxxjcrxxxxxxqx,2-5 r: xrrwx,9-13 j: rmxjjznzwgxsr,4-6 x: xxdlxv,2-4 l: tsflbprqxl,12-18 b: bbbbbbbbbbbbbbbbbbb,9-10 r: mjrzmtkrrw,2-14 d: dsddddddwvdjdvddd,2-3 z: bzfbfltzjjzk,7-9 g: gggggggggggg,3-5 c: cccccc,1-6 c: dtlfczchhc,5-10 w: wwbwtlwwwrjswwwphww,14-15 n: nnnnnnnnnnnnnnnnn,9-13 c: dbrssckbccfqhf,1-6 n: gsnnndncxnn,7-11 m: qpnmmjmmmbkgsl,10-14 g: pjgpsgzggggfggr,4-6 h: hhhhhh,12-16 c: clctqrpbnstchbpcbb,4-5 s: bmpssnwssxqsfzw,1-12 z: pqwzzzqbzzxx,10-11 r: rrrrrrrrrrrrrr,7-9 m: mmmmmsmrmmm,11-12 g: vmgnbfcggsqhn,2-5 k: kkkkk,18-19 x: qxxxxxxxtxxxhxxxxxx,10-11 v: vmvvvvvvvvpv,11-14 x: vxxsxjxxxxxxxx,4-13 m: bkmmsmdkxnfwj,4-5 s: smrsrvdllclvsgshldzs,12-15 b: kvdksbwdbqbbskb,1-4 p: bppc,1-4 t: tjtbqhjmf,1-2 n: tbrvn,1-2 p: ppppp,7-15 l: jlllllllllllllsllll,3-11 b: nbbgqhzqxhbwrbj,9-12 t: txfznwstgpttt,1-17 w: cfwwfwwwrwwlwwwbh,4-8 s: sssfrsss,8-13 r: tjmbdmzzhrrhdssssrt,1-11 h: ghxtbhktddm,2-14 m: dmshvpsdqjfvmv,4-10 l: lrwfrlbhvszjw,9-10 g: sgwcgtgvgg,13-19 l: cllllllllmllvllllvz,5-7 g: gggbfgvwpggg,14-18 p: fpwpxpsplkpsgprgpk,7-12 g: ggggggggggggg,10-12 v: vvkcvvdvvsvvv,1-8 x: xxxxxvxxxqx,13-20 r: rlfrgrblrsrrrhqjrbhr,9-12 z: cnhvszzzzhzbzcs,3-5 v: vvvdvvv,13-14 w: gpzwvcwwkwlkvr,1-4 v: vvvv,1-5 z: cszzlzzf,6-7 f: ffffqjn,2-4 z: xzzz,3-5 w: wwqlfwwkwshcfng,5-13 c: clccfcccccpcc,4-5 r: vrrrsrdvjrhbxxr,13-15 t: tgztttbtttcrtcq,7-8 c: cccccczmck,12-13 n: nnntlnnknnnhtnnnndnn,7-9 k: skfmkbkjkqckd,13-14 p: ppppppppppppvp,2-6 l: xlxzjlrdltzkclcmtrrq,3-5 l: xghjgvlljm,3-14 k: bkkkkkkkkkkkkkkk,13-15 d: rdddddddddddddddd,7-11 d: ddddddwdddnb,7-8 h: fhhhjhhh,6-9 z: mxzpxzzht,12-13 h: hghxnptwcnphhk,3-4 s: sswb,3-10 p: knpmvscqkpjpr,1-4 h: ghhr,11-12 k: klmkktfkkkkkzwfvkkkk,4-5 l: lkllv,13-14 n: nnnnnnnnnnnnsv,1-7 k: ktkkklk,3-4 n: nnxmnnq,13-14 b: bbbbbbsbbbbbbsbbbbb,3-4 q: qsgtqghlc,6-7 x: bmnhgxxjcxjqkv,5-10 k: hcvkkbkpqkdgmqthkc,4-9 k: kkkkkkkkkkkkkkkkkkk,1-3 q: qqqqfq,19-20 v: vvvvtvvvvvvvvvvvkvvv,3-4 w: knmw,17-18 c: ccdccccqccxcccwcgp,16-17 j: vhswszpdswjqmgwgjx,8-10 d: vfdbvlcddkdddddsd,4-15 q: nbbvqqqdlkgqbqrnqq,1-3 x: tvsxxhx,1-2 l: llcl,6-8 h: hhhhjphhwgmbr,7-8 z: gbzwzzln,2-16 k: hkhsgphcbnbnzljk,2-3 b: bgvbbbbbb,12-13 k: sqzkkdkrkkmwkw,3-6 r: ngrrjrrvrs,6-11 k: wqjtrzhkqjrqkkkq,4-8 w: wwwtwwsqwvwj,3-4 t: nqtt,5-13 h: hhhhdhhhhhhhghhhh,10-18 p: ppppppppppppppppppp,1-5 g: ggggmg,3-5 m: mmmmm,1-2 v: wmxlmzvk,6-10 f: vvlmfvfjjfgfwdsjw,15-18 g: kgggggggbggtggqggr,1-14 b: gkfbxwwfkdbtbgcnn,9-17 h: hmmhkttfhqpjhrhhhh,12-17 p: pptppppppppzppvpj,12-16 r: rbvvxkrrrrhrrmqrk,6-7 m: mmmmzmmmmxmmmgmmmd,8-10 n: jsnvzhdnnn,1-10 l: lllllllqblllllllll,10-11 s: sstswbsstndsv,1-3 w: wwwwwfs,4-7 c: ztxcphcqvsqwvlkcpp,5-6 z: zgnpgq,16-17 t: tgjtdjmppktjzwswt,6-7 r: kwcrrln,5-12 z: dzzgzsrzdfnx,12-16 z: qfzdrtjzzqzzbcnzzl,11-12 z: zfhdlzxqxzqc,13-16 s: sssslbsvsskssnbds,5-7 q: qqqqqqqqqqqdq,3-6 x: lxxrnx,2-9 r: rrdgvwztrq,14-17 t: tjtttttttttttttttttt,2-3 m: mxbbmmmm,14-16 j: jjjjjjjjjjcjjsjjj,1-12 l: plllllplljltllll,5-7 g: hgwzgdg,5-6 j: jwsjjzjjv,8-12 g: glxgcdxgrtgggcbhr,1-2 s: xslfpwnxkssps,4-7 v: vvvhvvvv,7-9 m: mwqmnsmdmmmmm,8-10 g: kgghgjgggggghggggggt,2-4 b: bbrbbvz,11-12 h: vhhvhhhvsmht,10-11 k: fjjvbvknvdkc,2-3 s: cssx,8-13 z: zzhzzzvzzzzzzxzq,3-11 v: jzvznwbfkvvdjrpwhjwp,4-11 n: qztnnqdrwznsdnbf,10-16 l: lllllllllllllllllkl,4-6 k: kkjmkk,5-19 t: wttttttdttttxgttrtt,6-7 k: kskkkqnkkkkkk,7-9 s: zsrkslsdsssrbm,5-6 k: vkwtrc,10-14 l: dllrldnvdlhlwl,10-13 k: kwkkkkmbkntktk,3-4 d: wdndd,1-3 h: tnwhj,4-7 k: vkjkkkkkhkp,4-7 f: fjjsfkw,7-8 p: ppppppwt,14-18 s: msqscsmssdssfszsjp,5-9 j: jjjjjjjjjjj,5-6 q: qlqqqqtxqxmqbsqqkqqq,9-11 t: wntvmlfctktp,2-17 r: rrrrsrdrrrcrrrrwrr,5-6 f: hqqftzf,1-6 x: dxxtptxx,11-12 m: gmhvmmbmmkgfl,13-15 s: ssssssssnmszsssqsl,7-8 h: hhhrhhhn,18-20 s: ssssssssssssssssshsb,5-8 h: hhlhhhth,9-14 w: bzbqgwwvwznjzwnpw,7-10 j: cjjgjljjjjjgxzb,2-5 c: cmcccc,8-9 t: tfxfcttst,3-4 s: psdz,3-4 w: wwwww,6-7 z: zzzrzzhzpzzzzz,1-8 m: mmmmmmmkmmmmmmmmmmn,6-8 g: gggggkglgg,7-17 w: wwwrxwcwkwrwdwvrsww,4-6 p: fzhpvvjcpcgj,5-6 s: ssssrv,3-12 m: wmmmlmhgxwvmhmh,6-7 k: ktkkmkhkkkj,10-17 z: zzzzzzzzzzzzzzzzzz,12-13 m: lmbpjkmhmmmwdm,5-6 x: xxxxxxxx,13-16 w: rxpgwwmzwpjcjbfkwws,2-9 q: gpbxlgjvnnpbxldqrvlc,6-9 j: xtzqzjntfmx,12-14 v: vcbvvvjvktvmdm,3-10 r: rrrrrcrrrrrrr,12-13 q: qqqqqqqqqsjvqq,6-8 k: kkkkkkkst,11-16 r: rjrrrrrrrrcrrrtr,1-7 t: ttkmvtvtqb,5-6 g: fljckdzhg,2-3 d: jxmk,6-7 g: gcgjgtg,8-16 h: ttkqfwskfpjrhcdm,9-10 d: ddddddddqtdddd,4-5 h: hhdzx,6-8 r: rvrrrrrqrr,9-11 j: gjjtmjjczjsj,1-3 s: ssssstsx,5-11 d: ddddldddddddd,4-9 b: bbbcbbhbqbbbbb,5-6 v: vrvvrfvvv,3-4 n: ngnvnn,15-17 q: fztljwtrzvphjqgkq,6-7 d: dddddddd,4-9 k: cvpckzdcqn,1-3 n: fnbn,3-7 j: jjdjjjjj,14-17 k: hjhrrkjkcbkkklhkbt,6-7 x: xdnbxcg,10-11 w: wwwwwwwwwjpww,1-9 k: kkkkkjkck,1-6 p: ppnpzppwbpprctgz,10-12 g: gqgggggggggggg,10-11 c: ccccccccccgc,11-12 r: rlrfzvrjbnqsjr,5-7 g: ggggzgg,13-17 q: qqqqqqqqqqqqqqqqdqqq,11-12 w: wwwwwwwwwwwww,9-10 q: qllqvqqqqsqqqqqnz,7-17 j: jjjjjhjjjjjjjjjjjjjj,1-2 h: hhhhh,19-20 f: ffwsqffffcdffnxjcvvd,1-14 p: pppgxppppspppppppfp,1-10 p: pmlrrfpppp,18-20 q: xqqqwmqgtcqnqqxgsqcq,1-8 z: zzjlbzkzzkzd,7-15 v: nvvkcsfplclzzch,4-8 g: bhmrqfgkkfxd,5-7 g: wggpqgs,3-9 p: pppmppczppcz,5-13 m: wmhmmmmhbfmmzc,3-4 p: ppjz,4-12 j: jtdjjvgvjnsjsbw,4-5 d: bdnddq,3-4 p: pjpppl,6-10 m: mkmmmrnmms,1-7 q: hlnfznrqqq,9-17 g: vvggrjhsgbsgwgbcg,1-5 q: mqqqq,1-3 g: nvgxtllpcgcgnmdqgg,1-3 z: wzsz,6-7 q: rfqqqrmwkqnqqq,3-6 d: zmhdnv,7-8 z: zljzzzzz,8-15 s: bnqsssshsspsssdsvsss,7-8 m: mmmmmmmm,5-6 t: ttttphtttt,6-17 v: jvbstgbwxnzvwmbvrm,12-19 z: pxtwzbrjqbczzbzfzdz,6-17 l: gvmwglltflqlrbbll,2-5 p: ppjhl,8-14 b: bbbbbbbbbbbbbbbb,15-16 g: ggmgdgnqgpdmggvq,8-12 x: xxxxxxxxxxxdx,1-2 h: hqjh,7-9 k: kkkkkkpkjkk,11-14 l: lzzlllfxlxlllq,3-4 d: kddd,6-14 x: xxxxnxxxxxxxxxgxxxx,8-10 m: mmmmmmmmmmm,5-12 s: ssswsjsszslsssssssss,3-9 r: rklrrrrxcrrrr,6-9 v: vvvvvpvvwvvvvvv,2-14 k: ndbbnhwdztdtkkjsvxc,4-5 w: wwjww,2-4 c: khcv,8-11 t: tttdtttcttttt,3-4 m: xmmmf"
   I IZ ADVENTpt2 YR INPUT MKAY BTW CALLS FUNCTION AND PRINTS RETURN VALUE

KTHXBYE