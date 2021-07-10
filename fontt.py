from .. import catub
normiefont = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
weebyfont = ['卂','乃','匚','刀','乇','下','厶','卄','工','丁','长','乚','从','𠘨','口','尸','㔿','尺','丂','丅','凵','リ','山','乂','丫','乙']
tantextfont = ['Ꭿ','Ᏸ','Ꮳ','Ꮄ','Ꮛ','Ꮄ','Ꮆ','Ꮒ','i','Ꮰ','Ꮶ','l','m','Ꮑ','Ꮻ','Ꮅ','Ꮔ','ᖇ','Ꭶ','Ꮏ','Ꮜ','Ꮙ','Ꮿ','ﾒ','Ꭹ','Ꮓ']
linetextfont = ['𝔸','𝔹','ℂ','𝔻','𝔼','𝔽','𝔾','ℍ','𝕀','𝕁','𝕂','𝕃','𝕄','ℕ','𝕆','ℙ','ℚ','ℝ','𝕊','𝕋','𝕌','𝕍','𝕎','𝕏','𝕐','ℤ']
boxtextfont = ['🄰','🄱','🄲','🄳','🄴','🄵','🄶','🄷','🄸','🄹','🄺','🄻','🄼','🄽','🄾','🄿','🅀','🅁','🅂','🅃','🅄','🅅','🅆','🅇','🅈','🅉']
bubbletextfont = ['Ⓐ','Ⓑ','Ⓒ','Ⓓ','Ⓔ','Ⓕ','Ⓖ','Ⓗ','Ⓘ','Ⓙ','Ⓚ','Ⓛ','Ⓜ','Ⓝ','Ⓞ','Ⓟ','Ⓠ','Ⓡ','Ⓢ','Ⓣ','Ⓤ','Ⓥ','Ⓦ','Ⓧ','Ⓨ','Ⓩ']
cursivefont = ['𝓪','𝓫','𝓬','𝓭','𝓮','𝓯','𝓰','𝓱','𝓲','𝓳','𝓴','𝓵','𝓶','𝓷','𝓸','𝓹','𝓺','𝓻','𝓼','𝓽','𝓾','𝓿','𝔀','𝔁','𝔂','𝔃'
]
nefont = [ '𝕒' ,'𝕓','𝕔','𝕕','𝕖','𝕗','𝕘','𝕙','𝕚','𝕛','𝕜','𝕝','𝕞','𝕟','𝕠','𝕡','𝕢','𝕣','𝕤','𝕥','𝕦','𝕧','𝕨','𝕩','𝕪','𝕫']

@catub.cat_cmd(pattern="dof ?(.*)")
async def weebify(ult):

    args = ult.pattern_match.group(1)
    if not args:
        get = await ult.get_reply_message()
        args = get.text   
    if not args:
        await ult.edit("What I am Supposed to Weebify? Please Give Text Sir")
        return
    string = ''.join(args).lower()
    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = nefont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)
    await ult.edit(string)