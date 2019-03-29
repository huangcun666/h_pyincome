from handlers.foo import FooHandler1,DemoHandler,IndexHandler,uploadHandler,mDemoHandler
from handlers.accounts import *
from handlers.sites import *
from handlers.guestbook import *
from handlers.img import *
from handlers.articles import *
from handlers.staticfile import *
from handlers.projects import *
from handlers.msg import *
from handlers.api import *
from handlers.category import *
from  handlers.milepost import *
from handlers.transition import *
from handlers.mobile import *
from handlers.receipt import *
from handlers.customer import *
from handlers.out import *
from handlers.accounts import *
from handlers.linkman import *
from handlers.contract import *
from handlers.finance import *
from handlers.mobile import *
from handlers.statis import *
from handlers.business_develop import *
from handlers.company import *
from handlers.plan import *
from handlers.account_receive import *
from handlers.payment import *
from handlers.addr import *
from handlers.displaylist import *
from handlers.clearly import *

url_patterns = [
    (r"/clearly", ClearlyHandler),
    (r"/plan", PlanHandler),
    (r"/company", CompanyHandler),
    (r"/statis", StatisHandler),
    (r"/mtransition", MTransitionHandler),
    (r"/category", CategoryHandler),
    (r"/mobile", MobileHandler),
    (r"/uploadpic", UploadPic),
    (r'/milepost', MilePostHandler),
    (r"/oapi", OApiHandler),
    (r"/capi", cAPiHandler),
    (r"/img", ImageHandler),
    (r"/foo", FooHandler1),
    (r"/de", DemoHandler),
    (r"/", mDemoHandler),
    (r"/msg", MsgHandler),
    (r"/upload", uploadHandler),
    (r"/api", ApiHandler),
    (r'/login', LoginHandler),
    (r'/logout', LogoutHandler),
    (r'/project', ProjectHandler),
    (r'/guestbook', GuestBookHandler),
    (r'/articles', ArticleHandler),
    (r'/news(?P<site_id>\d+)\_(?P<page>\d+).html', NewsHandler),
    (r'/post_(?P<id>\d+).html', NewsDetailHandler),
    (r'/changepassword', ChangePasswordHandler),
    (r'/allchangepassword', AllChangePasswordHandler),
    (r'/manageuser', ManageUserHandler),
    (r'/lockuser/(\d+)', LockUserhandler),
    (r'/unlockuser/(\d+)', UnlockUserHandler),
    (r'/insertuser', InsertUserHandler),
    (r'/changeuser', ChangeUserHandler),
    (r'/adminchangepassword/(\d+)', AdminChangePasswordHandler),
    # (r'/projectcategory',ProjectCategoryHandler),
    (r'/insertcategory', InsertCategoryHandler),
    (r'/insertupdateprojectcategory', InsertUpdateProjectCategoryHandler),
    (r"/upload_transition", TransitionUploadHandler),
    (r"/mobile", MobileHandler),
    (r"/uploadpic", UploadPic),
    (r"/finance", FinanceHandler),
    (r"/transition", CustomerTransitionHandler),
    (r"/linkman", LinkmanHandler),
    (r"/contract", ContractHandler),
    (r"/b", MainHandler),
    (r"/insert", InsertHandler),
    (r"/delete/(\d+)", DeleteHandler),
    (r"/change/(\d+)", ChangeHandler),
    (r"/changecustomer/(\d+)", ChangeCustomerHandler),
    (r"/customer_detail/(\d+)", CustomerdetailHandlder),
    (r"/detail/(\d+)", DetailHandler),
    (r"/newinsert", NewInsertHandler),
    (r"/customer", CustomerHandler),
    # (r"/", CustomerHandler),
    (r"/insert_customer", InsertcustomerHandler),
    (r"/customer_delete/(\d+)", CustomerdeleteHandler),
    (r"/searchdate", SearchDateHandler),
    (r"/out", OutHandler),
    (r"/insert_out", InsertOutHandler),
    (r"/out_delete/(\d+)", OutDeleteHandler),
    (r"/out_change/(\d+)", OutChangeHandler),
    (r"/outdetail/(\d+)", OutDetailHandler),
    (r"/business", BusinessHandler),
    (r"/account_receive", Account_receiveHandler),
    (r"/payment", PaymentHandler),
    (r"/addr", AddrHandler),
    (r"/displaylist", DisplayListHandler),

    # (r'/checkprojectcategory',CheckProjectCategoryHandler)
]
