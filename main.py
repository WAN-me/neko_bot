#!/bin/python3
import random

data = """https://avatars.mds.yandex.net/i?id=7ed47072176903c154a0632205397f6d_l-5232436-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=dbdda17ec77d86d1b51496bfaeb4ebda_l-5268509-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=11471ae5487b592b0364f4043ca538f9_l-5866055-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=e248ad0fb2a2787425e90725195ecae0_l-4872349-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=513d701acde4937d4d9401ea7fd498a7_l-5260797-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=811a13166238ae42b00f00452b0ccbb3_l-4417779-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=445e17943850ec7b4ab2a0443087e764_l-5579113-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=0b58d3182c3e4c18672db8cedf2e46dd_l-5192585-images-thumbs&n=13
https://ip1.anime-pictures.net/direct-images/c4a/c4a83cdb0bd75d5faa18cc3c6644ee83.png?if=ANIME-PICTURES.NET_-_612991-1091x1600-original-usagihime-single-long+hair-tall+image-looking+at+viewer.png
https://avatars.mds.yandex.net/i?id=eefc9c0d06e5d49977b1b3f9a1c274dc_l-5220466-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=3ca912a5d08fba33749ef7bd9c97353d_l-5240703-images-thumbs&n=13
https://cs11.pikabu.ru/post_img/big/2020/05/08/7/1588933039114792682.jpg
https://avatars.mds.yandex.net/i?id=4c94c28b6a9ad5f4248a30135128be96_l-4987702-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=9af3cfa51e9d4ae59ae3e7c9d4b7b2cc_l-5232515-images-thumbs&n=13
http://img10.reactor.cc/pics/post/full/Anime-%D1%8D%D1%82%D1%82%D0%B8-swim-%D0%AD%D1%82%D1%82%D0%B8-Strike-Witches-1883015.png
https://avatars.mds.yandex.net/i?id=5d783cd310d700fb699279bfcf8e09ec_l-5305969-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=d6b8daa700ee70b96cd391828a1ec350_l-5221936-images-thumbs&n=13
http://img10.reactor.cc/pics/post/Anime-Chen-Touhou-Project-Kaenbyou-Rin-5423880.png
https://avatars.mds.yandex.net/i?id=ced0880e82c4b4ffbe837cc090da99bb_l-5858580-images-thumbs&n=13
https://pibig.info/uploads/posts/2021-05/1620142639_3-pibig_info-p-koshkodevochki-etti-anime-krasivo-4.png
https://ip1.anime-pictures.net/direct-images/496/4965aad2610a0e62201e84f141fd0447.jpg?if=ANIME-PICTURES.NET_-_484077-857x1200-original-komori+kuzuyu-single-long+hair-tall+image-looking+at+viewer.jpg
https://avatars.mds.yandex.net/i?id=f9e017c8701a157db5941cd9c0f8e181_l-4570132-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=bb72c6473c2112963ddead4d8c54e29f_l-5255429-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=656f532fab364fb0d11122b238348ea1_l-5231332-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=2a2cb06a5f6597b4704e6733fab93ed8_l-5390142-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=306f9a152b2f585151bfebb88093846c_l-5363854-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=bfa05cabf1da3751655855f2434c8434_l-5110698-images-thumbs&n=13
https://pibig.info/uploads/posts/2021-05/1620142715_21-pibig_info-p-koshkodevochki-etti-anime-krasivo-23.png
https://avatars.mds.yandex.net/i?id=0cbe47cd4d9068abcc65287a308a48d8_l-5300120-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=91cf7b96ca710adeae270ccaeaa5c857_l-5673307-images-thumbs&n=13
https://i.ibb.co/0trSYVs/79000504-p0-master1200.jpg
https://avatars.mds.yandex.net/i?id=426eb76646a023d7efbe95b686203b71_l-5273845-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=c693bc73ed77a5519e47ef75213f1cd5_l-5315578-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=c878590f859c4856b87d34bb980e2068_l-5331866-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=792e2d37bb5a03ee3f8c19b2a55da734_l-5220947-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=c3f5a55b968507f3589756a3093597bd_l-5330362-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=a7c5fd4db149de77e3e8846a28a4f592_l-5338918-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=7e31983b0807e596b8dbcdf48b66ace4_l-4012918-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=921730fffbea3e77d29714c9909bdbc1_l-5876004-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=f273588240b61a3ac684006d2ad62196_l-5277189-images-thumbs&n=13
http://img2.reactor.cc/pics/post/full/Anime-Catgirl-4588947.jpeg
https://avatars.mds.yandex.net/i?id=ee3c9d6921fcc99950a3c8456592bea4_l-5889001-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=ddc9e120088be74f463b92648a6fecda_l-5876047-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=a68b9652bfc42d0fb77cb9faa87e6671_l-5255595-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=c49553efa170b825646b3e4327ded598_l-5240166-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=69359369ab5077d6c087e7a9df109d05_l-4076833-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=1f5661bb543fc004dcefbd6aa72c0bc8_l-5231845-images-thumbs&n=13
https://animesolution.com/wp-content/uploads/2019/12/Nekopara-OVA_38.55_2019.12.27_20.03.39_stitch-1536x1288.jpg
https://avatars.mds.yandex.net/i?id=7b7dd0192898a6b6b3244b92a0f9f068_l-5322158-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=87dd674e1fa64c73c285532025699c7f_l-2856395-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=91daaa94238848ba70290ff52b2d3c9f_l-5311590-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=6fed02e3a49c2e7974e992886524facf_l-4575620-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=780e907012f2edfe08af9c7b89b8ec9e_l-4559382-images-thumbs&n=13
https://pibig.info/uploads/posts/2021-10/1635188190_29-pibig-info-p-koshkodevochki-yuri-anime-krasivo-39.png
https://avatars.mds.yandex.net/i?id=12b444991c3f7ca41f2eadce025319b8_l-5253972-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=eb758f168af47220fa45c9cc9fcb3e67_l-5267851-images-thumbs&n=13
https://pibig.info/uploads/posts/2021-10/1635188239_35-pibig-info-p-koshkodevochki-yuri-anime-krasivo-45.png
https://avatars.mds.yandex.net/i?id=395951918ee8db7f3b3e9e66fee92932_l-5378083-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=f2aa820adcc6abc1dab56e8472b1cca9_l-5327796-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=3888b6bfb050dcf7bbf9390c8030ec94_l-5879932-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=b2eea42c9e5b234adb4f84cdffca48b3_l-5563308-images-thumbs&n=13
http://img2.reactor.cc/pics/post/neko-Animal-Ears-%28Anime%29-Anime-Matoi-Ryuuko-1101312.png
https://avatars.mds.yandex.net/i?id=d1f1488361a98df1c03dfa43224d5f09_l-5442358-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=aa60eb7038a376892da2129a425df3e4_l-4576832-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=9649294a7ed3663176eefcb6b00149ad_l-5221095-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=3d3be1fdf5e590003b1a594f83c76d1a_l-5018153-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=d2a8cef227cb049919347a789d635339_l-5323018-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=0113829a9e881c9099ea59a2416c58bb_l-5258962-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=d78e7f9b493714f214417e9d9d228f72_l-5234843-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=c7f9ff6b329d64a85bd2dba5969f0175-5601751-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=0740e83dd10fd4f728e1d62679a6fe66_l-5234483-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=de095b27c0ebf2633c22b7dfbb530242_l-5235635-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=5aa38f2ad06026cf1429c72db706a857_l-5213357-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=664ce1e492ef791df3d14dd689a2ad2c_l-5232907-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=0b293263062bdd3bce81aff2f2fafa2a_l-5321633-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=69d48291a866f0d3a80101ba142735e7_l-5231880-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=79c6b73f1ca9e959efe9a46d9617e72e_l-4471740-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=db16d9b6228107272befc0f11939e4f2_l-5285713-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=6ef6b66d788b08b57cee5bc602812d77_l-5221012-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=2946abf4a14246667aaf9ce770f33932_l-4033947-images-thumbs&n=13
https://get.wallhere.com/photo/neko-loli-animal-ears-tail-in-bed-long-hair-short-hair-1397321.jpg
https://avatars.mds.yandex.net/i?id=fb1aa58a97162339071aa61d647e7a8d_l-5353565-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=9bc17ae57765626b1607a8359b385003_l-5591414-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=d8846ee3501a22f839ddfdfa1788f577_l-5367334-images-thumbs&n=13
https://kartinkin.net/uploads/posts/2021-07/thumbs/1626151893_7-kartinkin-com-p-chokola-i-vanilla-anime-anime-krasivo-7.png
https://avatars.mds.yandex.net/i?id=9631b73629d1b9ab9e424372d3dd05a1_l-5233500-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=bd45c742b62bb21e00fdb17e608a2d7a_l-5348026-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=787ae710005e807699f63f14453d0033_l-4113862-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=9d5ada271d3fd14e20c8ebb9a4759c3e-4024741-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=6cb3324a23cd33218444cbaf33bd5135_l-5220773-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=f478ed9be22c20930a6d7ba9c29196a8_l-5285349-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=cc55ce36586cba75dbc4fc320f0970e2_l-5233506-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=9562736b5aa572bfcb4af92635a8d6ea_l-3514751-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=7fe49b8b530bffa88e11b0d053edd92e_l-4519223-images-thumbs&n=13
https://static.zerochan.net/Dido.%28Azur.Lane%29.full.2857940.png
https://avatars.mds.yandex.net/i?id=19a8d2f7d1456e911e600b64175a7cda_l-5234007-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=12d82172c464d7b15ee18e71b1ee7b20_l-5221767-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=c5b96cfce44d895fc6453993c4fcb006_l-5031045-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=a66e767b7b0a71f73faf2b03f2143f20_l-5294162-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=b7ab73b27ac4a3437eb8a521b100d3e7_l-5292558-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=e9cb4b9024a95873ec1bcec059975710_l-5578090-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=255c48bc295782d7ee6c394be04d8741_l-3514751-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=891a7e349209f7ccad439548339f6d36_l-5339388-images-thumbs&n=13
http://www.animei.pl/wp-content/uploads/2016/02/Kocia-bielizna-manga-555x783.png
https://avatars.mds.yandex.net/i?id=3b76df2bef8062e15d4d03fb7f06b09a_l-5209122-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=fbff9aaded28d7fb1d1ab9fb611c1d06_l-5333993-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=be113efa658ca0b2f408c4cbc9ec8540_l-5285663-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=4af693bf628c19d8656aef5fdfc665b6_l-5233468-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=ef51371fa68de9327e8a7daac88d1750_l-5283209-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=4d6634f9cc6e6eb78605c17c43dbda06_l-5234389-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=5d2d6c68447f8169165dda4fb0e34d63_l-5247043-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=af796a9b1baf8b17e7ee29b8885cb474_l-5222025-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=28ee42caa90614ba5b25b30affdbb219_l-4522636-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=6ad6be37741cd8e3f4758eb7d0611e44_l-5334643-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=a3c171de79fe38f51d2161eadffed9d8_l-5363193-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=e34186926f17882a025449c3f2a9df35_l-5283209-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=0641553ff05b03ff49f99da431dece29_l-5130185-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=17e6afc07150a51268663fbbf98f7856_l-5355514-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=5e4b0f1e15c78533f01ccf912b3193c7_l-5211841-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=54d338f316f692e6ba6db8a7750ee618_l-5313814-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=287adee6f209613aa35dc2c3ce8bf857_l-5232766-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=f46a42ac6fdc97382af8443c96895726_l-5289357-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=7a5b5333a1b1075cb9ac2cb22f66897b_l-5220772-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=16dc012195fd81c1bd3020ea97d2ae32_l-5209680-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=8f4b88af8763aef12073ad968ec0edfb_l-5233466-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=28175af102567533ed7cadb9003b8560_l-5331782-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=52dd70494876cae8e5f27e1a30329744_l-5232436-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=3ea317df269cd7a50e88e98bdad37937_l-5354608-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=94118eb05d67938df29e1cde0daa348e_l-4827339-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=9f00fc79f09cb7a1f730d101b6e1d9b8_l-5168030-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=984c9857e6af1a9a42c6affa90f5d25c_l-5345654-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=8a43b6f99b9993eff44289c782cc1cbf_l-5342121-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=01dbc17ca3dc36015f496ebea8f7b369_l-5224693-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=2a7d150952ff1403946129f0e7bc925b_l-3001461-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=e5836def246ae582e6705b52fb1f969d_l-5295477-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=2149f73b003ca35520628d1370fdadeb_l-5286572-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=0ce706441c6d40f88ca7f6ef98b558f6_l-5222505-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=ca91c2ebfbebe2c4606d092e2a5d1043_l-5231718-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=fd49237f1ff9629e948df813516be5c6_l-4447708-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=23e1f568317ea3f9d1dae11480ffb962_l-5239602-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=02a4106ed1e7709befb0bbbdf673e6f6-5233519-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=a979c09888fe68529d37ae8aa8068d32_l-5231013-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=5325ce1a3b83ca5efe6009be305b50df_l-4012866-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=c37befc0f0a5597fdad76999869c93f9_l-5232826-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=183610486ff9302a8f88e34ef5a9c00c_l-5242458-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=54bcdc6333bc5522a947defb64cc9918_l-5276366-images-thumbs&n=13
http://img10.reactor.cc/pics/post/full/AO-Anime-Art-Anime-neko-5189554.png
https://avatars.mds.yandex.net/i?id=6a85cd7fdaf6a1f63249f806e119c739_l-5231826-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=3b90128c477a879cc6a3b5d7048e66ac_l-5234460-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=83ed3ecac6d5ecbd92b4ca21c0cf2df4_l-4569097-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=d17913af6370181d1b8f6498c1459280_l-5233099-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=70f37b811db55841ffcd0b71c8b18895_l-5288148-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=2ad3c62ed2d147cdc7a291e0a1b4f70c_l-5194042-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=c8539e4b547efb2e8c4df1fa9aac039d_l-5145180-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=91a008ccc11f97deb62c68a8d99cccfc_l-5288900-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=dbafd62e56a6c3ec45a970fdfae4d51b_l-4837630-images-thumbs&n=13
https://cdn140.picsart.com/324966150172211.png
https://avatars.mds.yandex.net/i?id=e3cb3fa8af5d5ca443c30b84888280ec-5219738-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=16245b8e02b883255dd998259eda167f_l-5336145-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=26a2e508c69259b78112ccac4b8d3f32-4821375-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=17fb535fe4ab7e423541e0758e1caec5_l-5251742-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=6b6afc3bad6ffe66ab8376b39d6303a3_l-4304327-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=8312a0b82d30acd4d11dd5e6652adf21_l-4266310-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=ad50aa4cb29deaa510ee24a35ad546be_l-5434889-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=dad187b96985c165fecb41d042dce5ab_l-5233147-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=bcb7d6b6105e7bb99d5ef9b59d06b1c0_l-5433602-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=e9b788dd1ae5123938566dd8a40f7cfd_l-5251456-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=6056753065b624c369abaaa7bb04c459_l-5314093-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=1d3034ead352bf8b4110666885436fdb_l-5234042-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=382f74ceac0ea75e61eac97ad8e22354_l-5289438-images-thumbs&n=13
https://safebooru.org/images/2578/e900e0d5faaf076636c0f50b682ce925f8eaeefa.png?2685803
https://avatars.mds.yandex.net/i?id=5866034ab8a8fcf3bfaacd89f96c6ece_l-5327407-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=b155d5b668513640f876a40d728fedc0_l-5235511-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=44b5acd798c537bfe451913640b878ea_l-4987526-images-thumbs&n=13
https://ip1.anime-pictures.net/direct-images/6a0/6a0b28617a1ae376fac468d7a658cf0b.png?if=ANIME-PICTURES.NET_-_388270-2123x3009-neko+paradise-neko+works+04+%28artbook%29-vanilla+%28nekopara%29-chocola+%28nekopara%29-sayori-long+hair.png
https://avatars.mds.yandex.net/i?id=db3ee51e358b089310c5e9b480565758_l-5254684-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=b7b9fcb2a9dcdf5c224cce9dc2b3f051_l-5246115-images-thumbs&n=13
https://i.imgur.com/FMuNyPk.jpg
https://avatars.mds.yandex.net/i?id=1ae390d49f12d97a7a219974e328c36d_l-5248827-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=94232ab7c7da85b07a9fbfe31a85f2bf_l-4113862-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=3651808f0f503c2ff28aebee35b6cdea_l-5220454-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=54c515b5608cc615e8ceb343594cd3b3_l-5347001-images-thumbs&n=13
https://static.zerochan.net/Love.Live%21.full.2278002.png
https://avatars.mds.yandex.net/i?id=657c6b145b2eaffdd5afc2a12674284b_l-3888471-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=f7c45f248c139d76939ac71c9785878b_l-4824599-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=c905a3bdbb44357cd419f53bb1f6d57a_l-5382665-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=a9d5068bf76caef0ee9a94316454cd46_l-5248085-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=5d46608b44b59f1d1c1d559dc84984c6_l-5347144-images-thumbs&n=13
https://pibig.info/uploads/posts/2021-10/1635188252_47-pibig-info-p-koshkodevochki-yuri-anime-krasivo-60.png
https://avatars.mds.yandex.net/i?id=946dcab62dae8ab122bd62f4ccaf85ac_l-5441329-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=b23fb732b7646210f761516581383b10_l-5236000-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=94041ee4af56ab95dbbcde2662632e5a_l-5161023-images-thumbs&n=13
https://images6.alphacoders.com/787/787462.png
https://avatars.mds.yandex.net/i?id=8fd518efd8ac3d2299d333e11d6fbd54_l-5292008-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=7f7a6a897ed8bb34c483d47cd942f776_l-3613310-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=5a70ab26deee7cc419d5b11c7d6aed79_l-5382326-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=dd072890071f1982d787028888df1b33_l-4290022-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=f65b1eb5a0b0a34bf0142a50da22bbfe_l-5228381-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=e656fca79c14da289222b28ca5986371_l-5578090-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=a260ae23ea6c02c2d88c2812cdd963d2_l-5221157-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=37cd09cdb55a9a2cbb388b3224d8c1c0_l-5296066-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=b6825c2fb611b302045283bdc6faee04_l-5237855-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=96aa67250014698550675ff013e5a8e5_l-5228069-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=9d4efa8d7704bd2dc1ba35fc84568657_l-5275502-images-thumbs&n=13
http://img10.reactor.cc/pics/post/full/Re-Zero-Kara-Hajimeru-Isekai-Seikatsu-Anime-Rem-%28re-zero%29-Ram-%28Re-Zero%29-3529083.png
https://avatars.mds.yandex.net/i?id=7f519fdafc781401091d1725d1b1e426_l-4482255-images-thumbs&n=13
https://ip1.anime-pictures.net/direct-images/878/8783092097c7aa1ec11c961d93671039.png?if=ANIME-PICTURES.NET_-_558138-1085x1535-azur+lane-akagi+%28azur+lane%29-kaga+%28azur+lane%29-akagi+%28paradise+amaryllis%29+%28azur+lane%29-kaga+%28everlasting+killing+stone%29+%28azur+lane%29-kaetzchen.png
https://avatars.mds.yandex.net/i?id=739b602a032b60a5b3950b642ae04cd6_l-3071791-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=989c30f3982ad184c4bb5bca54f89c6e_l-5338555-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=2fc5db255536460d90fad7dbc2c3c62d_l-5746783-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=2f2ff23f00db298683f6a9fb99e7ec98_l-5162869-images-thumbs&n=13
https://papik.pro/uploads/posts/2021-09/1630746430_17-papik-pro-p-anime-koshkodevochka-risunok-20.png
https://avatars.mds.yandex.net/i?id=23c31496b2ee5376d5d01a72417aca46_l-4620768-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=1ef62523e4a7b250528642c7dbfff7de_l-5265420-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=095fee9b118540f029e710b13e174806_l-5235366-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=8f934bcd24784de98220f66046cb1827_l-5344395-images-thumbs&n=13
https://krot.info/uploads/posts/2021-03/1614631292_20-p-devushka-v-chernom-kupalnike-art-kartinki-31.png
https://avatars.mds.yandex.net/i?id=2c006d93571e2f8a40de69812142a4a6_l-5307135-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=1c583662a99b1a724e3230df733ecb51_l-5350728-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=1f76c9cd8732c9ed6d1d74a98c36a689_l-5288898-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=49ec5f7d44f051938415da2bfec8d117_l-5232263-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=75af1ef63a4fb21b7da869645b3bc94a_l-5210592-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=cf1f1f608439e8d90f6fc98837084879_l-5218303-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=86bda2406e66eaf986ce9d01d1860f6b_l-5215694-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=0ea5d11aebb88467df88f63f937a9402_l-5252183-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=af8c2cee42d77554303aedba72d0ea2a_l-5254505-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=d4ea1e6e38f70db25f5b0a6b140ade0c_l-5221961-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=c6d34f0700e0b3736c01857ffb0e8974_l-5210240-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=a1b77287e47a74af90943e28ad2726bb_l-5282838-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=fab59beb75daae23fd2f77c454c1361c_l-5236639-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=5938e2a3ccb931c3299dbeb1df1c731a_l-5344395-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=66c01a632a31ada3cc0d9c58a07e5677_l-5481835-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=9ee27d98c44446193fc964880751e359_l-5233468-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=95235b17382c8c248a92a3c9b3672246_l-5336145-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=efaa2e15ddc72f63ae38b116b19b8e32_l-5268893-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=f8c63fe16705d41713a86ff37401fb43_l-5228102-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=2861e2bd1a225be49e3a124a0a76a381_l-4866825-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=b0e4c5acee6283e6396e786c69daea78_l-4079679-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=800db512b183f559d44bd5a8c912572b_l-4298620-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=b9d69514a9282f53b9539c7e9a2fab34_l-5209520-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=ec06a68581723b35dc9d0b67260dc817_l-5170901-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=a63c00f92dc921913aaa75b8352ed370_l-5026383-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=a592416f064a623e7369a0518c054ab4_l-4707222-images-thumbs&n=13
https://static.zerochan.net/Saeki.Sola.full.2439940.png
https://avatars.mds.yandex.net/i?id=ff3633b7d49eefe8ff0f42ec35171a2d_l-5236812-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=ee153bdf892a307f7675b4d3eda304ec_l-5277308-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=9d666edfb29d1173a12c1ece69955890_l-4219938-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=80b5f67c9ed1c3471c9409d79472f292_l-5340195-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=cacfda25c612e121886e750d9c7d493c_l-5103244-images-thumbs&n=13
https://get.wallhere.com/photo/anime-girls-anime-cat-girl-thigh-highs-original-characters-animal-ears-1375899.jpg
https://avatars.mds.yandex.net/i?id=f66bd09113f569302b2822c47016aaed_l-4219929-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=6f037408c173b83a4e0155143f71cbde_l-5235619-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=cac18320bbeedd6d221ae873daf221a5_l-4827941-images-thumbs&n=13
https://i.imgur.com/CTqJ69F.png
https://avatars.mds.yandex.net/i?id=838de5054aac4c92ec191554c8ae29a9_l-5249255-images-thumbs&n=13
https://ip1.anime-pictures.net/direct-images/d89/d89c64a740124166f15e3b4ea8f67480.png?if=ANIME-PICTURES.NET_-_499671-3000x3500-original-utaka+%28anyoanyot%29-single-long+hair-tall+image-looking+at+viewer.png
https://avatars.mds.yandex.net/i?id=7c1105877c0d28c60cf79c1ed9eec102_l-5381936-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=adaffdf76642bbd764561a5d63722cba_l-4568203-images-thumbs&n=13
https://cdn140.picsart.com/298718906180211.png
https://avatars.mds.yandex.net/i?id=73aa0f16bce9a26493596e77ec6fbd5a_l-5236416-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=00f3511aee8a46cedee3ba1364b77341_l-5238336-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=8e2d40042f5dc2d12d1f91511ddae391_l-4576346-images-thumbs&n=13
https://c.wallhere.com/photos/de/bc/anime_anime_girls_Love_Live_cat_girl_Nishikino_Maki_Yazawa_Nico_cat_keyhole_bra_nekomimi-1374047.jpg!d
https://avatars.mds.yandex.net/i?id=bf71b1cce1da3340ee338e68990b19e5_l-4900962-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=d2cc35945c3c2e94480d3fb5a6d49707_l-5233787-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=4689bf16af6117489367bab30d9225f3_l-5324012-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=caee2215008ddb8afc9f641da2bc4d59_l-5333794-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=dcb6017f5ca084978793a1bf84326a3d_l-5295477-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=4e5939b7403eb1f5c65c25b1abd9ab40_l-5331218-images-thumbs&n=13
https://www.goha.ru/s/E:Mb/nG/n2HU1ggjCG.jpg
https://avatars.mds.yandex.net/i?id=b46bf9b365dba4b5c673d21123b187d1_l-5229051-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=f06606304e32088d43b4b202c4c71aa8_l-5298752-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=86bfd50fb694086c5e3f9a9348e0839c_l-5256718-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=1583d4194747eb0e3a0014a8790fac80_l-5213143-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=f4e25e2ff001078b03f5dd20194ee3d8_l-5239483-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=af340ce8bfd31a742ccebf5214e7a141_l-5345102-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=aa45042ceaa8f3682740d4e53747324e_l-5288661-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=c0e5fbf18c14527f62554a0dcf60d4c2_l-5275190-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=6324753deb1ace988cb31f09d5f14a57_l-5348787-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=6df259954eef929f2fb68afc6f525ab5_l-5425154-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=cf508e42e91a1b92d2392a3db59b8efd-5273666-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=51571f6e96c26acf934e5f2f7644f997_l-4575945-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=8c81a0f0a268ddcae52db52c6872c99d_l-4575767-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=b53614b99224df70789262dac7be0c39_l-5141122-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=ab5ddc8db2ff450ea2cf498ed81f749d_l-5286572-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=05c08754bfd675481b97e4b7eb684a61_l-4719838-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=2e5401fad37047ad8c2001c16c860fb5_l-5218274-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=38b61715ee2c5793368b1ff5260e40dc_l-5042534-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=89517ccb6b4bbae16fa8789ec7ed492a_l-5348623-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=bdf51ad2632cb94c3d168b76cb1a31ef_l-5345654-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=03b90edf70fecd2d4e71e6e3245b23f3_l-5224721-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=6fd5b55bad74f7b93c1df65fc37f5c6a_l-5346024-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=4d1b8c36b96ce61d5d3be98727d276f3_l-5232914-images-thumbs&n=13
https://ip1.anime-pictures.net/direct-images/8fb/8fbc3cce6d2125516b094d6950d39481.png?if=ANIME-PICTURES.NET_-_470567-827x1280-kantai+collection-hamakaze+destroyer-alphe-single-tall+image-blush.png
https://avatars.mds.yandex.net/i?id=f431018192b4e802b85cc797cab95191_l-5222388-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=e3cb9df43467a3007fb709ce09ac2228_l-4842027-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=5db7ed534309bf1261517414f97c3169_l-5221656-images-thumbs&n=13
https://avatars.mds.yandex.net/i?id=799c7a825228ed281697a39fdd19a433_l-5331218-images-thumbs&n=13""".split('\n')
import telebot



def _send(chatid, text, pm='HTML',):
    print(text)
    if len(text) < 4096:
        bot.send_message(chat_id=chatid,
                         parse_mode=pm,
                         text=text)  # Отправка текста
    else:
        ofset = 0
        while ofset < len(text):
            bot.send_message(chat_id=chatid, parse_mode=pm,
                             text=text[ofset:ofset + 4096])
            ofset += 4096

TOKEN = ""

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def get_text_messages(msg):
    print(msg.json)
    text = msg.json.get('text','0')
    if text[0] in ['.', '/', '\\', '!', '_']:
        url = random.choice(data)
        if random.randint(1,100) > 50:
            _send(msg.chat.id, f'<a href="{url}">Держи, милый</a>')
        else:
            _send(msg.chat.id, f'Я не в настроении')
    elif random.randint(1,100) > 96:
        url = random.choice(data)
        _send(msg.chat.id, f'<a href="{url}">Ня</a>')


if __name__ == "__main__":
    print('starting...')
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
    print('exiting...')


