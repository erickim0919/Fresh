#!/usr/bin/python3

import cgi
import random


def htmlTop():
    print('''Content-type:text/html\n\n
        <!DOCTYPE html>
        <html dir="ltr" lang="en-US">
        <head>

            <meta http-equiv="content-type" content="text/html; charset=utf-8" />
            <meta name="author" content="Eric Kim" />

            <!-- Stylesheets
            ============================================= -->
            <link href="http://fonts.googleapis.com/css?family=Noto+Sans:400,700|Noto+Serif:400,700" rel="stylesheet" type="text/css" />
            <link rel="stylesheet" href="css/bootstrap.css" type="text/css" />
            <link rel="stylesheet" href="style.css" type="text/css" />
            <link rel="stylesheet" href="css/dark.css" type="text/css" />

            <link rel="stylesheet" href="css/font-icons.css" type="text/css" />
            <link rel="stylesheet" href="css/animate.css" type="text/css" />
            <link rel="stylesheet" href="css/magnific-popup.css" type="text/css" />

            <link rel="stylesheet" href="css/responsive.css" type="text/css" />
            <meta name="viewport" content="width=device-width, initial-scale=1" />

            <link rel="stylesheet" type="text/css" href="include/rs-plugin/css/settings.css" media="screen" />
            <link rel="stylesheet" type="text/css" href="include/rs-plugin/css/layers.css">
            <link rel="stylesheet" type="text/css" href="include/rs-plugin/css/navigation.css">

            <link rel="stylesheet" type="text/css" href="include/rs-plugin/css/addons/revolution.addon.liquideffect.css">

            <link rel="stylesheet" href="css/colors.php?color=267DF4" type="text/css" />
            <link rel="stylesheet" href="main/recipes/css/fonts.css" type="text/css" />
            <link rel="stylesheet" href="main/recipes/recipes.css" type="text/css" />
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

            <style>
                .dt-shadow{text-shadow:0px 10px 30px rgba(0,0,0,1)}#rev_slider_131_1 .uranus.tparrows{width:50px; height:50px; background:rgba(255,255,255,0)}#rev_slider_131_1 .uranus.tparrows:before{width:50px; height:50px; line-height:50px; font-size:40px; transition:all 0.3s;-webkit-transition:all 0.3s}#rev_slider_131_1 .uranus.tparrows:hover:before{opacity:0.75}.slotholder canvas { height: 100% !important; }
                .checked {
                    color: orange;
                        }
            </style>

            <title>Contact | Fresh</title>

        </head>

        <body class="stretched">

            <!-- Document Wrapper
            ============================================= -->
            <div id="wrapper" class="clearfix">

                <!-- Header
                ============================================= -->
                <header id="header" class="transparent-header static-sticky clearfix">

                    <div id="header-wrap">

                        <div class="container clearfix">

                            <div id="primary-menu-trigger"><i class="icon-reorder"></i></div>

                            <!-- Logo
                            ============================================= -->
                            <div id="logo" class="">
                                <a href="index.html" class="standard-logo"><img src="main/recipes/images/fresh_logo.JPG" alt="Fresh Logo"></a>
                                <a href="index.html" class="retina-logo"><img src="main/recipes/images/fresh_logo.JPG" alt="Fresh Logo"></a>
                            </div>

                            <!-- Primary Navigation
                            ============================================= -->
                            <nav id="primary-menu">

                                <ul>
							        <li class="current"><a href="index.html"><div>Home</div></a></li>
							        <li><a href="main/recipes/about-us.html"><div>About Us</div></a></li>
							        <li><a href="main/recipes/recipes.html"><div>Recipes</div></a></li>
							        <li><a href="main/recipes/contact-test.html"><div>Contact Us</div></a></li>
						        </ul>

                            </nav><!-- #primary-menu end -->

                        </div>

                    </div>

                </header> <!-- #header end --> 

                <section id="content" style="overflow: inherit;">

                    <div class="content-wrap pb-0">

                        <div class="section mt-2 nobg">
                            <div class="container">
                                <div class="row">
                                    <div class="col-md-8 offset-2 center">
                                        <h2 class="text-title-light text-dark mb-5 ls1 uppercase">Thank you for your input!</h2>
                                        <p style="font-size: 17px; color: #777"> Welcome to the family! The Fresh Team will try their best to reply to your question/comment as soon as possible. In the meantime, check out our other recipes! <br><br>Cheers to all your cooking endeavors!</p>
                                        <img src="main/recipes/images/signature.JPG" alt="Signature" width="250" class="mt-3">
                                    </div>

                            </div>
                        </div>
                    </div>
                </section>        
            </div>           
             <script src="js/jquery.js"></script>
             <script src="js/plugins.js"></script>
             <script src="include/rs-plugin/js/jquery.themepunch.tools.min.js"></script>
             <script src="include/rs-plugin/js/jquery.themepunch.revolution.min.js"></script>
             <script src="include/rs-plugin/js/pixi.min.js"></script>
             <script src="include/rs-plugin/js/addons/revolution.addon.liquideffect.min.js"></script>
             <script src="js/functions.js"></script>

             <script>
                 var revapi2,
                 tpj;
                 (function() {
                    if (!/loaded|interactive|complete/.test(document.readyState)) document.addEventListener("DOMContentLoaded",onLoad); else onLoad();

                    function onLoad() {
                        if (tpj===undefined) { tpj = jQuery; if("off" == "on") tpj.noConflict();}
                            if(tpj("#rev_slider_2_1").revolution == undefined){
                                revslider_showDoubleJqueryError("#rev_slider_2_1");
                            }else{
                                revapi2 = tpj("#rev_slider_2_1").show().revolution({
                                    sliderType:"standard",
                                    jsFileLocation:"include/rs-plugin/js/",
                                    sliderLayout:"fullscreen",
                                    dottedOverlay:"none",
                                    delay:9000,
                                    parallax: {
                                        type:"scroll",
                                        origo:"slidercenter",
                                        speed:400,
                                      speedbg:0,
                                      speedls:0,
                                        levels:[5,10,15,20,25,30,35,40,45,46,47,48,49,50,51,55],
                                    },
                                    navigation: {
                                        keyboardNavigation:"off",
                                        keyboard_direction: "horizontal",
                                        mouseScrollNavigation:"off",
                                         mouseScrollReverse:"default",
                                        onHoverStop:"off",
                                        arrows: {
                                            style:"uranus",
                                            enable:true,
                                            hide_onmobile:false,
                                            hide_onleave:false,
                                            tmp:'',
                                            left: {
                                                h_align:"right",
                                                v_align:"bottom",
                                                h_offset:80,
                                                v_offset:30
                                            },
                                            right: {
                                                h_align:"right",
                                                v_align:"bottom",
                                                h_offset:20,
                                                v_offset:30
                                            }
                                        }
                                    },
                                    responsiveLevels:[1240,1024,778,480],
                                    visibilityLevels:[1240,1024,778,480],
                                    gridwidth:[1240,1024,778,480],
                                    gridheight:[868,768,960,720],
                                    lazyType:"all",
                                    shadow:0,
                                    spinner:"off",
                                    stopLoop:"off",
                                    stopAfterLoops:-1,
                                    stopAtSlide:-1,
                                    shuffle:"off",
                                    autoHeight:"off",
                                    fullScreenAutoWidth:"off",
                                    fullScreenAlignForce:"off",
                                    fullScreenOffsetContainer: "70",
                                    fullScreenOffset: "",
                                    disableProgressBar:"off",
                                    hideThumbsOnMobile:"off",
                                    hideSliderAtLimit:0,
                                    hideCaptionAtLimit:0,
                                    hideAllCaptionAtLilmit:0,
                                    debugMode:false,
                                    fallbacks: {
                                        simplifyAll:"off",
                                        nextSlideOnWindowFocus:"off",
                                        disableFocusListener:false,
                                    }
                                });
                            };

                            RsLiquideffectAddOn(tpj, revapi2);

                            if(typeof ExplodingLayersAddOn !== "undefined") ExplodingLayersAddOn(tpj, revapi2);
                        };
                    }());
             </script>       ''')


def htmlTail():
    print ('''</body>
        </html>''')

def getData():
    form = cgi.FieldStorage()
    cname = form.getvalue("contactname")
    cemail = form.getvalue("contactemail")
    cphone = form.getvalue("contactphone")
    csubject = form.getvalue("contactsubject")
    cmessage = form.getvalue("contactmessage")
    ccopy = form.getvalue("contactcopy")

    dorm = open("contactuslist.txt", "a")
    dorm.write(str(cname)+"\n")
    dorm.write(str(cemail)+"\n")
    dorm.write(str(cphone) + "\n")
    dorm.write(str(csubject) + "\n")
    dorm.write(str(cmessage)+"\n")
    dorm.write(str(ccopy)+"\n")

       
def main():
    htmlTop()
    print(''.format(getData()))
    htmlTail()


if __name__ == '__main__':
    try:
        main()
    except:
        cgi.print_exception()
