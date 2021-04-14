#api_key = api key here

# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import pickle


MAX_CHANNELS = 20   # Zero based counter

# channel ids for each category
list_channel_ids_1 = ["UC5tuYcCdiKuF5Y2ZonuarwA", "UC8-Th83bH_thdKZDJCrn88g", "UCNVBYBxWj9dMHqKEl_V8HBQ",
                       "UCUR8Hid3gm05upmtk4LrgpQ", "UC3uTUlmgECBnsP777U4GPKQ", "UCP84QWij0alw4MvzqzyfOnw",
                       "UCsv4YOF2RBYh0NQ1vuHQ-hg", "UCDwbDyYQGQuLcyr0_gv1IeQ", "UCPeZTzsoQ4iBjfkVbU0ilmg",
                       "UCnoqvTW4YZExfDeq7_Wmd-w", "UCkAGrHCLFmlK3H2kd6isipg", "UCwWhs_6x42TyRM4Wstoq8HA",
                       "UC4-eGDvOe41__-RiE0E9L6A", "UCt4atlExw8aj3Bm79nv1fig", "UCn3AViOfcFN4zIICMC5hvPg",
                       "UC0PKLLmL8pIJLjOI1gBH_pA", "UCE1V4pxb_e1_6XLrOGflPPA", "UCXbYlU08sOTBktOtjVsvR6w",
                       "UC0zXnLIFedO97pFsyMxZcFg", "UCpsSadsgX_Qk9i6i_bJoUwQ"]

list_channel_ids_2 = ["UCbCmjCuTUZos6Inko4u57UQ", "UCBnZ16ahKA2DZ_T5W0FPUXg", "UCcdwLMPsaU2ezNSJU1nFoBQ",
                       "UCKAqou7V9FAWXpZd9xtOg3Q", "UCLsooMJoIpl_7ux2jvdPB-Q", "UCRx3mKNUdl8QE06nEug7p6Q",
                       "UCsPF3cApzCohxPp5oKdoWSQ", "UCpYye8D5fFMUPf9nSfgd4bA", "UC7Pq3Ko42YpkCB_Q4E981jw",
                       "UCR-foyF-C6VuAlwy3KZMkgA", "UC6zPzUJo8hu-5TzUk8IEC2Q", "UCsXVk37bltHxD1rDPwtNM8Q",
                       "UCuWuAvEnKWez5BUr29VpwqA", "UCsooa4yRKGN_zEE8iknghZA", "UC1zZE_kJ8rQHgLTVfobLi_g",
                       "UCHN9P-CQVBQ1ba8o1NQJVCA", "UC6zhI71atP7YLoZyIyCIGNw", "UCX6b17PVsYBQ0ip5gyeme-Q",
                       "UC5PYHgAzJ1wLEidB58SK6Xw", "UCC552Sd-3nyi_tk2BudLUzA"]

list_channel_ids_3 = ["UCk8GzjMOrta8yxDcKfylJYw", "UCJplp5SjeGSdVdwsfb9Q7lQ", "UCvlE5gTbOvjiolFlEm-c_Ow",
                       "UCppHT7SZKKvar4Oc9J4oljQ", "UCX6OQ3DkcsbYNE6H8uQQuVA", "UCZJ7m7EnCNodqnu5SAtg8eQ",
                       "UCYvmuw-JtVrTZQ-7Y4kd63Q", "UCp0hYYBW6IMayGgR-WeoCvQ", "UCcgqSM4YEo5vVQpqwN-MaNw",
                       "UCS94J1s6-qc8v7btCdS2pNg", "UC55IWqFLDH1Xp7iu1_xknRA", "UCstEtN0pgOmCf02EdXsGChw",
                       "UCgFXm4TI8htWmCyJ6cVPG_A", "UChGJGhZ9SOOHvBB0Y4DOO_w", "UCU2zNeYhf9pi_wSqFbYE96w",
                       "UCpko_-a4wgz2u_DgDgd9fqA", "UCJ0uqCI0Vqr2Rrt1HseGirg", "UCpB959t8iPrxQWj7G6n0ctQ",
                       "UCucot-Zp428OwkyRm2I7v2Q", "UCaWd5_7JhbQBe4dknZhsHJg"]

list_channel_ids_4 = ["UC3gNmTGu-TTbFPpfSs5kNkg", "UCPNxhDvTcytIdvwXWAm43cA", "UCAOtE1V7Ots4DjM8JLlrYgg",
                       "UCu59yAFE8fM0sVNTipR4edw", "UCUe6ZpY6TJ0no8jI4l2iLxw", "UCUAL--p3qAa27luR0IYbjZA",
                       "UCK5Q72Uyo73uRPk8PmM2A3w", "UCX_uPA_dGf7wXjuMEaSKLJA", "UC9trsD1jCTXXtN3xIOIU8gg",
                       "UCi8e0iOVk1fEOogdfu4YgfA", "UCdxi8d8qRsRyUi2ERYjYb-w", "UCFeUyPY6W8qX8w2o6oSiRmw",
                       "UCbKWv2x9t6u8yZoB3KcPtnw", "UCHCph-_jLba_9atyCZJPLQQ", "UC7e1XWjOlYy8XlNMeVxeKNg",
                       "UCzIdYMdAtTsWucGCZyZvN6w", "UCK8bPFkXVfr_czCIEmZ8zYQ", "UC3sznuotAs2ohg_U__Jzj_Q",
                       "UCGwu0nbY2wSkW8N-cghnLpA", "UCzrMFWFWPou9RCMufXwWdDg"]

list_channel_ids_5 = ["UC-lHJZR3Gqxm24_Vd_AJ5Yw", "UCV4xOVpbcV8SdueDCOxLXtQ", "UC7_YxT-KID8kRbqZo7MyscQ",
                       "UCYzPXprvl5Y-Sf0g4vX-m6g", "UCKqH_9mk1waLgBiL2vT5b9g", "UCS5Oz6CHmeoF7vSad0qqXfw",
                       "UCAW-NpUFkMyCNrvRSSGIvDQ", "UCDCNmuaOXOo25Yn4mbMHhhQ", "UCvh1at6xpV1ytYOAzxmqUsA",
                       "UC0DZmkupLYwc0yDsfocLh0A", "UC5c9VlYTSvBSCaoMu_GI6gQ", "UCC-RHF_77zQdKcA75hr5oTQ",
                       "UCw1SQ6QRRtfAhrN_cjkrOgA", "UCYVinkwSX7szARULgYpvhLw", "UCpGdL9Sn3Q5YWUH2DVUW1Ug",
                       "UCD1Em4q90ZUK2R5HKesszJg", "UC4hGmH5sABOA70D4fGb8qNQ", "UCke6I9N4KfC968-yRcd5YRg",
                       "UCTkXRDQl0luXxVQrRQvWS6w", "UCKy1dAqELo0zrOtPkf0eTMw"]

list_channel_ids_6 = ["UC295-Dw_tDNtZXFeAPAW6Aw", "UC4rlAVgAK0SGk-yTfe48Qpw", "UCWwqHwqLSrdWMgp5DZG5Dzg",
                       "UCJFp8uSYCjXOMnkUyb3CQ3Q", "UC2etEuPIfohP4P53wM0KImA", "UC57XAjJ04TY8gNxOWf-Sy0Q",
                       "UCkvK_5omS-42Ovgah8KRKtg", "UCCgLoMYIyP0U56dEhEL1wXQ", "UC03RvJoIhm_fMwlUpm9ZvFw",
                       "UCR4s1DE9J4DHzZYXMltSMAg", "UCzTKskwIc_-a0cGvCXA848Q", "UCjwmbv6NE4mOh8Z8VhPUx1Q",
                       "UC2WuPTt0k8yDJpfenggOAVQ", "UCo6DJdltbIub80bLiyJRv3w", "UCuN4A3GCUq5-0wJDSiJoxRQ",
                       "UCAoMPWcQKA_9Af5YhWdrZgw", "UCWRV5AVOlKJR1Flvgt310Cw", "UC0YvTCy1I4_a-3pn47_5DBA",
                       "UCmRY4NSGK52lP_Lz11CjdYw", "UCZGcvm26TfY3g1EQ-ohXBvg"]

list_channel_ids_7 = ["UCbCmjCuTUZos6Inko4u57UQ", "UCk8GzjMOrta8yxDcKfylJYw", "UCJplp5SjeGSdVdwsfb9Q7lQ",
                       "UCvlE5gTbOvjiolFlEm-c_Ow", "UCBnZ16ahKA2DZ_T5W0FPUXg", "UCcdwLMPsaU2ezNSJU1nFoBQ",
                       "UC4NALVCmcmL5ntpV0thoH6w", "UCS94J1s6-qc8v7btCdS2pNg", "UCKAqou7V9FAWXpZd9xtOg3Q",
                       "UCgFXm4TI8htWmCyJ6cVPG_A", "UChGJGhZ9SOOHvBB0Y4DOO_w", "UCRx3mKNUdl8QE06nEug7p6Q",
                       "UCKqx9r4mrFglauNBJc1L_eg", "UCDCNmuaOXOo25Yn4mbMHhhQ", "UCAOtE1V7Ots4DjM8JLlrYgg",
                       "UCsPF3cApzCohxPp5oKdoWSQ", "UCpYye8D5fFMUPf9nSfgd4bA", "UCu59yAFE8fM0sVNTipR4edw",
                       "UC_8PAD0Qmi6_gpe77S1Atgg", "UCoookXUzPciGrEZEXmh4Jjg"]

list_channel_ids_8 = ["UCq-Fj5jknLsUf-MWSy4_brA", "UCFFbwnve3yF62-tVXkTyHqg", "UCIwFjwMjI0y7PDBVEO9-bkQ",
                       "UCOmHUn--16B90oW2L6FRR3A", "UCEdvpU2pFRCVqU6yIPyTpMQ", "UC3IZKseVpdzPSBaWxBxundA",
                       "UC0C-w0YjGpqDXGB8IHb662A", "UC9CoOnJkIBMdeijd9qYoT_g", "UCfM3zsQsOnfWNUppiycmBuw",
                       "UCqECaJ8Gagnn7YCbPEzWH6g", "UCbuK8xxu2P_sqoMnDsoBrrg", "UCJrOtniJ0-NWz37R30urifQ",
                       "UCiGm_E4ZwYSHV3bcW1pnSeQ", "UCbTLwN10NoCU4WDzLf1JMOA", "UCJrDMFOdv1I2k8n9oK_V21w",
                       "UCb2HGwORFBo94DmRx4oLzow", "UCBVjMGOIkavEAhyqpxJ73Dw", "UCHkj014U2CQ2Nv0UZeYpE_A",
                       "UCM9r1xn6s30OnlJWb-jc3Sw", "UCa10nxShhzNrCE1o2ZOPztg"]

list_channel_ids_9 = ["UCRWFSbif-RFENbBrSiez1DA", "UCIvaYmXn910QMdemBG3v1pQ", "UCupvZG-5ko_eiXAupbDfxWw",
                       "UCBi2mrWuNuyYy4gbM6fU18Q", "UCZFMm1mMw0F81Z37aaEzTUA", "UCLXo7UDZvByw2ixzpQCufnA",
                       "UC16niRr50-MSBwiO3YDb3RA", "UCfwx98Wty7LhdlkxL5PZyLA", "UC9k-yiEpRHMNVOnOi_aQK8w",
                       "UC1NF71EwP41VdjAU1iXdLkw", "UCNye-wNBqNL5ZzHSJj3l8Bg", "UCXIJgqnII2ZOINSWNOGFThA",
                       "UCMmpLL2ucRHAXbNHiCPyIyg", "UClFSU9_bUb4Rc6OYfTt5SPw", "UCZaT_X_mc0BI-djXOlfhqWQ",
                       "UC11PvrGPzo6Y7Zc6-e9cAKg", "UCeY0bbntWzzVIaj2z3QigXg", "UC1yBKRuGpC1tSM73A0ZjYjQ",
                       "UC25Ntv5IrTD-B0eZ92O50Tg", "UC69uYUqvx-vw4luuX7aHNLQ"]

list_channel_ids_10 = ["UCsT0YIqwnpJCM-mx7-gSA4Q", "UCsrRPShwtgobdwkglhQVlDw", "UCdNjexbIS_NKJC4ZRwKf9ag",
                       "UCYv-siSKd3Gn9IsliO95gIw", "UCQ0gG42bXPBi7yHx9UJyexQ", "UCjQbTcszB-gRhDByY9WhySw",
                       "UCg3_C7BwcV0kBlJbBFHTPJQ", "UCBP4B896svWOcWdRp8UjH2Q", "UCh4pyZUB0mNzieaKv831flA",
                       "UCMrKscEv_Ri1pvlRsLxsqJQ", "UCX4kkW2kc-x_3EbbkxhZZLw", "UCVBohU3S3fKk-pagBqYsfaQ",
                       "UCB7BryuXaMe1pUMznYAq4Jg", "UCc4yillQaNo6a-iG2PYbbrA", "UCXKseLTu1Pbyc99wB8bGkug",
                       "UC5MDIy3yhWDrx0MyDo4QmYg", "UCXL6kvDyoQpvtaeafC4pLyg", "UCaZX9C1LPOpzsJfZe5BxDjw",
                       "UC07-dOwgza1IguKA86jqxNA", "UCnrFlpro0xfYjz6s5Xa8WWw"]

list_channel_ids_11 = ["UCYLNGLIzMhRTi6ZOLjAPSmw", "UCcgVECVN4OKV6DH1jLkqmcA", "UCpko_-a4wgz2u_DgDgd9fqA",
                       "UCWwWOFsW68TqXE-HZLC3WIA", "UCmh5gdwCx6lN7gEC20leNVA", "UC-SV8-bUJfXjrRMnp7F8Wzw",
                       "UCNL1ZadSjHpjm4q9j2sVtOA", "UCCI5Xsd_gCbZb9eTeOf9FdQ", "UCGXUFnA7-MzlMwJjl0r2qyA",
                       "UC4-CH0epzZpD_ARhxCx6LaQ", "UCjmAh2qxmvWdH3xNPbg0IUQ", "UCtinbF-Q-fVthA0qrFQTgXQ",
                       "UCja7QUMRG9AD8X2F_vXFb9A", "UCkXgEcpoTE4tHsebYBouWpA", "UCI78AdiI6f7VKhqW1i4B3Rw",
                       "UCypeLkg3Ne5-LIyiB41b1GQ", "UC0Kgvj5t_c9EMWpEDWJuR1Q", "UCwIWAbIeu0xI0ReKWOcw3eg",
                       "UCVbPnm-qCjH-8Yl1-k4BQkA", "UCay_OLhWtf9iklq8zg_or0g"]

list_channel_ids_12 = ["UC6E2mP01ZLH_kbAyeazCNdg", "UCC7tqA6lA2QRw4BdrAEKFxg", "UCGCPAOQDZa_TTTXDr5byjww",
                       "UCwmZiChSryoWQCZMIQezgTg", "UCINb0wqPz-A0dV9nARjJlOQ", "UC4kyYTypYb3mQ6ZL25kly6g",
                       "UCdu8QrpJd6rdHU9fHl8J01A", "UCNo5PGwGmfnEprEUUb9AGgw", "UCVUdHi-tdW5AKdzMiTPG97Q",
                       "UC6zbH1Z4G32bBV9wyK6ikPA", "UCsmxCQDcT9Tb6WchlS5Of0Q", "UCI8FQkQ-Iv73GZcsJ-6pNWw",
                       "UCONd1SNf3_QqjzjCVsURNuA", "UCKy3MG7_If9KlVuvw3rPMfw", "UC9z6M5AhkOkAasrl2hKlVAw",
                       "UC7MCFUG5oKKsfVDl7gT7BRA", "UC9gPwVGWqT8xkArzQ2PB0jA", "UCZ-oMIRggrNuzsWLtNFXBXw",
                       "UCKD8QcX1LhFB8n7lhjfuQdg", "UCZzFRKsgVMhGTxffpzgTJlQ"]

list_channel_ids_13 = ["UCqsS8fU6yVxrJr5y_CoUn3w", "UCAuUUnT6oDeKwE6v1NGQxug", "UCsTcErHg8oDvUnTzoqsYeNw",
                       "UC6nSFpj9HTCZ5t-N3Rm3-HA", "UCY1kMZp36IQSyNx_9h4mpCg", "UCE_M8A5yxnLfW0KghEeajjw",
                       "UCBJycsmduvYEL83R_U4JriQ", "UCXuqSBlHAE6Xw-yeJA0Tunw", "UCe_vXdMrHHseZ_esYUskSBw",
                       "UCjgpFI5dU-D1-kh9H1muoxQ", "UCSiDGb0MnHFGjs4E2WKvShw", "UCZdGJgHbmqQcVZaJCkqDRwg",
                       "UCAL3JXZSzSm8AlZyD3nQdBA", "UCK8sQmJBp8GCxrOtXWBpyEA", "UC6107grRI4m0o2-emgoDnAA",
                       "UCDRx0wMgscsG6vPNB0sO65Q", "UCj34AOIMl_k1fF7hcBkD_dw", "UC1tVU8H153ZFO9eRsxdJlhA",
                       "UCLA_DiR1FfKNvjuUpBHmylQ", "UC4Tklxku1yPcRIH0VVCKoeA"]

list_channel_ids_14 = ["UCqH2YMSzMaGN92Vc3VkhWnQ", "UC7hH2YyQqtECP5o4_atzYHA", "UCqKjymEVHOUR_60HMCzSVdA",
                       "UCxbGH9vwaYY4hd2Pb-UArLw", "UC73A9DqkczBxUHHiDbDwwtA", "UCccjdJEay2hpb5scz61zY6Q",
                       "UCqf2gzmKtH3PaAbt-qgFFsw", "UCrNnk0wFBnCS1awGjq_ijGQ", "UCWJ2lWNubArHWmf3FIHbfcQ",
                       "UCqOoboPm3uhY_YXhvhmL-WA", "UCkEBDbzLyH-LbB2FgMoSMaQ", "UCBUzq54I6EJl84nxm12ImDQ",
                       "UC08wrceRCWhajGG4udhETww", "UCpVm7bg6pXKo1Pr6k5kxG9A", "UCqAEL720vsR0NHe3ZRLN4Mw",
                       "UC8Y-jrV8oR3s2Ix4viDkZtA", "UC4AjFz9s-Snm1wN8hh8DnWQ", "UCQugQycuz3Fn-DgesSLT_fg",
                       "UCJUAqHnkDX15IvFoXIGTm2A", "UCqqTQy4ZyJNnqpevVfTTXzw"]


list_channel_ids_15 = ["UCJ5v_MCY6GNUBTO8-D3XoAg", "UCRijo3ddMTht_IHyNSNXpNQ", "UCWJ2lWNubArHWmf3FIHbfcQ",
                       "UCKvn9VBLAiLiYL4FFJHri6g", "UCI4fHQkguBNW3SwTqmehzjw", "UC14UlmYlSNiQCBe9Eookf_A",
                       "UCvgfXK4nTYKudb0rFR6noLA", "UCqhnX4jA0A5paNd1v-zEysw", "UCblfuW_4rakIf2h6aqANefA",
                       "UCpcTrCXblq78GZrTUTLWeBw", "UCBvc7pmUp9wiZIFOXEp1sCg", "UCC9h3H-sGrvqd2otknZntsQ",
                       "UCiWLfSweyRNmLpgEHekhoAg", "UCDVYQ4Zhbm3S2dlz7P1GBDg", "UCdPui8EYr_sX6q1xNXCRPXg",
                       "UCkBY0aHJP9BwjZLDYxAQrKg", "UCqjwF8rxRsotnojGl4gM0Zw", "UC8pYaQzbBBXg9GIOHRvTmDQ",
                       "UCTv-XvfzLX3i4IGWAm4sbmA", "UCWV3obpZVGgJ3j9FVhEjF2Q"]


list_channel_ids_16 = ["UCyEd6QBSgat5kkC6svyjudA", "UCcAd5Np7fO8SeejB1FVKcYw", "UCHKVXtT1YBCYUnnr4apqXfg",
                       "UCiAq_SU0ED1C6vWFMnw8Ekg", "UCXOKEdfOFxsHO_-Su3K8SHg", "UCixvwLpO_pk4uVOkkkqP3Mw",
                       "UCwiTOchWeKjrJZw7S1H__1g", "UCxDZs_ltFFvn0FDHT6kmoXA", "UCvWulTmPsyUscivbwE-xg2Q",
                       "UCfYCRj25JJQ41JGPqiqXmJw", "UC0Ize0RLIbGdH5x4wI45G-A", "UCRFj4Yj1nKhgrT-_8AUsaDg",
                       "UC9avFXTdbSo5ATvzTRnAVFg", "UCVrvnobbNGGMsS5n2mJwfOg", "UCt_NLJ4McJlCyYM-dSPRo7Q",
                       "UC4ijq8Cg-8zQKx8OH12dUSw", "UCGSLH_5EGpS2eEkjEOkZLIg", "UCT-LpxQVr4JlrC_mYwJGJ3Q",
                       "UCixD9UbKvDxzGNiPC_fgHyA", "UCu9g5OmzcCpcJnmSYyHnIVw"]


lci1 = [list_channel_ids_1,list_channel_ids_2, list_channel_ids_3, list_channel_ids_4] #these lists are made due to the api quota
lci2 = [list_channel_ids_5, list_channel_ids_6, list_channel_ids_7, list_channel_ids_8, list_channel_ids_9]
lci3 = [list_channel_ids_10, list_channel_ids_11, list_channel_ids_12, list_channel_ids_13, list_channel_ids_14]
lci4 = [list_channel_ids_15, list_channel_ids_16]

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def get_vid_ids(channel_ids): # a function from google api that gets 50 video ids from each channel id
    return_list = []
    for id in channel_ids:
        request = youtube.search().list(
            part="snippet",
            channelId=id,
            maxResults=50,
            order="viewCount",
            type="video",
            videoDefinition="any",
            videoDimension="any",
            videoDuration="any",
            videoEmbeddable="any",
            videoLicense="any",
            videoSyndicated="any",
            videoType="any"
        )
        response = request.execute()
        return_list.append(response)
    return return_list

def write_ids_to_file(start_num, subidslist): # we write all the information we extract to the pickled file (for each category 50 ids are stored)s
    for i in range(len(subidslist)):
        vid_ids = get_vid_ids(subidslist[i])
        filename = "cat"+str(start_num + i)+"ids.lst"
        f = open(filename, "wb")
        pickle.dump(vid_ids, f)
        f.close()
def magic_data_extracter(start_num, subidslist):
    list_video_ids = []
    for i in range(len(subidslist)):
        counter = 0
        id_list = []
        filename = "cat"+str(start_num + i)+"ids.lst" # Important
        file=pickle.load(open(filename, 'rb'))
        for channel_index in range(MAX_CHANNELS):
            videoinfolist = file[channel_index]["items"]
            for video_index in range(len(videoinfolist)):
                id_list.append(videoinfolist[video_index]["id"]["videoId"])
                counter +=1
        list_video_ids.append(id_list)
        print("Channel list "+str(i)+" has "+str(counter)+" videos and has a deficit of "+str(1000-counter)+" videos.")
    print(list_video_ids)
    f = open("videoids"+str(start_num+(i-4))+".lst", "wb")
    pickle.dump(list_video_ids, f)
    f.close()

# Disable OAuthlib's HTTPS verification when running locally.
# *DO NOT* leave this option enabled in production.

######### Toggles, do not change unless you know what you are doing!!##########
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
authmode=1
getmode=0  #Write mode is getmode = 0, This gets the videoid data from Youtube
           # Read mode is getmode = 1, This extracts the videoids into videoids.lst
###############################################################################
if getmode: #using the functions together to get data and write them to pickled videoids.lst
    magic_data_extracter(0, lci1)

else:
    api_service_name = "youtube"
    api_version = "v3"

    if authmode:
        client_secrets_file = ### insert your authentication here
    else:
       client_secrets_file =  ### insert your authentication here

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    write_ids_to_file(0, lci1)

