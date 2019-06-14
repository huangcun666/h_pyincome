#coding=utf8
#提取确认单角色 {% raw get_member(item.mbs,"销售顾问")%}{%end%}
def get_member(mbs,team_name):
        return_s = ""
        if mbs:
            for r in mbs.split(","):
                if r:
                    mb = r.split("|")
                    if mb[0]==team_name :
                        if mb[1] in return_s:
                            continue
                        if return_s :
                            return_s +=","
                        return_s+= mb[1]
                        

        return return_s