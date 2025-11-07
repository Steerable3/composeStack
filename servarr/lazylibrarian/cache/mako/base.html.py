# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1762071045.7481713
_enable_loop = True
_template_filename = '/app/lazylibrarian/data/interfaces/bookstrap/base.html'
_template_uri = 'base.html'
_source_encoding = 'utf-8'
_exports = ['javascriptIncludes', 'headIncludes', 'headerIncludes']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        title = context.get('title', UNDEFINED)
        style = context.get('style', UNDEFINED)
        next = context.get('next', UNDEFINED)
        perm = context.get('perm', UNDEFINED)
        __M_writer = context.writer()

        import lazylibrarian
        from lazylibrarian.common import docker
        from lazylibrarian.config2 import CONFIG
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['lazylibrarian','docker','CONFIG'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n<!doctype html>\n<html>\n  <head>\n    <meta http-equiv="content-type" content="text/html; charset=UTF-8">\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n    <title>LazyLibrarian - ')
        __M_writer(str(title))
        __M_writer('</title>\n    <meta name="description" content="">\n    <meta name="author" content="">\n    <meta name="viewport" content="width=device-width, initial-scale=1" />\n    <link rel="shortcut icon" type="image/png"  href="images/ll.ico">\n    <link rel="apple-touch-icon" href="images/ll.png">\n    <link rel="manifest" href="images/manifest.json">\n    <link rel="stylesheet" type="text/css" href="css/datatables.min.css"/>\n')
        if lazylibrarian.BOOKSTRAP_THEMELIST:
            __M_writer('    <link id="theme" href="https://maxcdn.bootstrapcdn.com/bootswatch/3.3.7/')
            __M_writer(str(style))
            __M_writer('/bootstrap.min.css" rel="stylesheet">\n')
        else:
            __M_writer('    <link href="css/bootstrap.min.css" rel="stylesheet">\n')
        __M_writer('    <!--link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.13/css/all.css" integrity="sha384-DNOHZ68U8hZfKXOrtjWvjxusGo9WQnrNx2sqG0tfsghAvtVlRW3tvkXWZh58N9jp" crossorigin="anonymous"-->\n    <link href="css/fontawesome/fontawesome-all.css" rel="stylesheet">\n    <link href="css/bookstrap.css" rel="stylesheet">\n    <style>\n      input[type="search"]::-webkit-search-cancel-button {\n      -webkit-appearance: none;\n      height: 16px;\n      width: 16px;\n      margin-left: .4em;\n      background-image: url("data:image/svg+xml;utf8,<svg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 24 24\' fill=\'%23777\'><path d=\'M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z\'/></svg>");\n      cursor: pointer;\n    }\n    </style>\n    <script src="js/jquery-3.4.1.min.js"></script>\n    <script src="js/lazylibrarian-bs.js"></script>\n\n    <!-- include summernote css/js -->\n    <link href="css/summernote.css" rel="stylesheet">\n    <script src="js/summernote.js"></script>\n\n    ')
        __M_writer(str(next.headIncludes()))
        __M_writer('\n    <script type="text/javascript">\n      if(navigator.userAgent.toLowerCase().indexOf(\'firefox\') > -1){\n        // Allow the user to reset the search filter\n        // (-webkit-search-cancel-button does not work on firefox)\n        $(document).ready(function () {\n            $.fn.dataTableExt.oApi.clearSearch = function ( oSettings ) {\n                var table = this;\n                var clearSearch = $(\'<i id="Clear" title="Clear" class="fa fa-times" style="height:20px;width:20px;vertical-align:center;cursor:pointer;">&nbsp;</i>\');\n                $(clearSearch).click( function () {\n                                table.fnFilter(\'\');\n                                $(\'input[type=search]\').val(\'\');\n                });\n                $(oSettings.nTableWrapper).find(\'div.dataTables_filter\').append(clearSearch);\n                $(oSettings.nTableWrapper).find(\'div.dataTables_filter label\').css(\'margin-right\', \'-20px\');\n                $(oSettings.nTableWrapper).find(\'div.dataTables_filter input\').css(\'padding-right\', \'20px\');\n            }\n            //auto-execute, no code needs to be added\n            $.fn.dataTable.models.oSettings[\'aoInitComplete\'].push( {\n                "fn": $.fn.dataTableExt.oApi.clearSearch,\n                "sName": \'whatever\'\n            });\n        });\n      }\n    </script>\n\n    ')
        __M_writer(str(next.javascriptIncludes()))
        __M_writer('\n    <script type="text/javascript">\n      // Check or uncheck all checkboxes in the same table\n      function toggleAll(e) {\n          var table = $(e).closest(\'table\');\n          $(\'td input:checkbox\', table).trigger("click");\n      }\n    </script>\n    <script type="text/javascript" src="js/bootstrap.min.js"></script>\n    <script type="text/javascript" src="js/datatables.min.js"></script>\n    <script type="text/javascript" src="js/natural.js"></script>\n    <script type="text/javascript" src="js/bootbox.min.js"></script>\n    <script type="text/javascript" src="js/bootstrap-notify.min.js"></script>\n<style>\n\n#show_newz_prov {display:  none; }\n#show_newz_prov + label::before { content: \'\\f107\'; }\n#show_newz_prov:checked + label::before { content: \'\\f106\'; }\n#show_torz_prov {display:  none; }\n#show_torz_prov + label::before { content: \'\\f107\'; }\n#show_torz_prov:checked + label::before { content: \'\\f106\'; }\n#show_tor_prov {display:  none; }\n#show_tor_prov + label::before { content: \'\\f107\'; }\n#show_tor_prov:checked + label::before { content: \'\\f106\'; }\n#show_rss_prov {display:  none; }\n#show_rss_prov + label::before { content: \'\\f107\'; }\n#show_rss_prov:checked + label::before { content: \'\\f106\'; }\n#show_irc_prov {display:  none; }\n#show_irc_prov + label::before { content: \'\\f107\'; }\n#show_irc_prov:checked + label::before { content: \'\\f106\'; }\n#show_direct_prov {display:  none; }\n#show_direct_prov + label::before { content: \'\\f107\'; }\n#show_direct_prov:checked + label::before { content: \'\\f106\'; }\n\n#myBtn {\n  display: none;\n  position: fixed;\n  bottom: 10px;\n  right: 15px;\n  z-index: 99;\n  font-size: 18px;\n  border: none;\n  outline: none;\n  background-color: #888;\n  color: white;\n  cursor: pointer;\n  padding: 6px;\n  border-radius: 4px;\n  opacity: 0.4;\n  filter: alpha(opacity=40); /* For IE8 and earlier */\n}\n\n#myBtn:hover {\n  background-color: #555;\n  opacity: 1.0;\n  filter: alpha(opacity=100); /* For IE8 and earlier */\n}\n#Clear:hover {\n  color: #555;\n  opacity: 1.0;\n  filter: alpha(opacity=100); /* For IE8 and earlier */\n}\n\n#myAlert {\n  display: block;\n  position: fixed;\n  bottom: 48px;\n  right: 15px;\n  z-index: 99;\n  font-size: 14px;\n  border: 2px solid lightgrey;\n  outline: none;\n  background-color: #888;\n  color: white;\n  cursor: pointer;\n  padding: 6px;\n  border-radius: 8px;\n  opacity: 0.4;\n  filter: alpha(opacity=40); /* For IE8 and earlier */\n}\n\n#myAlert:hover {\n  background-color: #555;\n  opacity: 1.0;\n  filter: alpha(opacity=100); /* For IE8 and earlier */\n}\n\n#log_type{\n  min-width: 90px;\n}\n\n#log_label{\n  min-width: 70px;\n}\n@media screen  and (min-width: 768px)and (max-width: 1024px) {\n    /* Add a pseudo-element with the\n       text from attribute \'data-abbr\' */\n    .shorten[data-abbr]::after {\n        content: attr(data-abbr);\n    }\n\n    /* Hide the original label */\n    .shorten > span { display: none; }\n}\n</style>\n</head>\n  <body>\n    <div id="container">\n      <header>\n        <div id="headercontainer" class="navbar navbar-default navbar-fixed-top">\n          <div class="container">\n            <div class="navbar-header">\n              <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#MainNav" aria-expanded="false">\n                <span class="sr-only">Toggle navigation</span>\n                <span class="icon-bar"></span>\n                <span class="icon-bar"></span>\n                <span class="icon-bar"></span>\n              </button>\n              <a class="navbar-brand" href="home"><i class="fa fa-home"></i> LazyLibrarian</a>\n            </div>\n            <div class="collapse navbar-collapse" id="MainNav">\n              <ul class="nav navbar-nav">\n                <!--li><a href="home" class="navbarele">Authors</a></li-->\n')
        if perm > 0:
            pass
            if CONFIG['USER_ACCOUNTS']:
                pass
                if lazylibrarian.SHOWLOGOUT == 1:
                    __M_writer('                      <li><a href="logout" class="navbarele" id="logout">Logout</a></li>\n')
                if perm&lazylibrarian.perm_config == 0:
                    __M_writer('                      <li><a href="profile" class="navbarele" id="profile">User</a></li>\n')
        if CONFIG['HOMEPAGE'] != 'Authors':
            __M_writer('                  <li><a id="authors" href="authors" class="navbarele">Authors</a></li>\n')
        if CONFIG['HOMEPAGE'] != 'eBooks':
            pass
            if CONFIG['EBOOK_TAB']:
                pass
                if perm&lazylibrarian.perm_ebook:
                    __M_writer('                  <li><a id="books" href="books" class="navbarele">eBooks</a></li>\n')
        if CONFIG['HOMEPAGE'] != 'Series':
            pass
            if CONFIG['SERIES_TAB']:
                pass
                if perm&lazylibrarian.perm_series:
                    __M_writer('                  <li><a id="series" href="series" class="navbarele">Series</a></li>\n')
        if CONFIG['HOMEPAGE'] != 'AudioBooks':
            pass
            if CONFIG['AUDIO_TAB']:
                pass
                if perm&lazylibrarian.perm_audio:
                    __M_writer('                  <li><a id="audio" href="audio" class="navbarele">\n                  <div class="shorten" data-abbr="Audio">\n                      <span>AudioBooks</span>\n                  </div>\n                  </a></li>\n')
        if CONFIG['HOMEPAGE'] != 'Magazines':
            pass
            if CONFIG['MAG_TAB']:
                pass
                if perm&lazylibrarian.perm_magazines:
                    __M_writer('                  <li><a id="magazines" href="magazines" class="navbarele">\n                  <div class="shorten" data-abbr="Mags">\n                      <span>Magazines</span>\n                  </div>\n                  </a></li>\n')
        if CONFIG['HOMEPAGE'] != 'Comics':
            pass
            if CONFIG['COMIC_TAB']:
                pass
                if perm&lazylibrarian.perm_comics:
                    __M_writer('                  <li><a id="comics" href="comics" class="navbarele">Comics</a></li>\n')
        if perm&lazylibrarian.perm_managebooks:
            pass
            if CONFIG['AUDIO_TAB']:
                __M_writer('                    <li><a id="amanage" href="manage" class="navbarele">Manage</a></li>\n')
            elif CONFIG['EBOOK_TAB']:
                __M_writer('                    <li><a id="emanage" href="manage" class="navbarele">Manage</a></li>\n')
        if perm&lazylibrarian.perm_history:
            __M_writer('                  <li><a id="history" href="history" class="navbarele">History</a></li>\n')
        if perm&lazylibrarian.perm_logs:
            __M_writer('                  <li><a id="logs" href="logs" class="navbarele">Logs</a></li>\n')
        if perm&lazylibrarian.perm_config:
            __M_writer('                  <li><a id="config" href="config" class="navbarcfg"><i class="fa fa-cog"></i> Config</a></li>\n')
        __M_writer('                <li><a id="help" href="help" target="_new"><i class="fa fa-question-circle"></i> Help</a></li>\n              </ul>\n            </div>\n          </div>\n          <div id="subnav" class="navbar-inverse">\n            <div id="subhead" class="container">\n              ')
        __M_writer(str(next.headerIncludes()))
        __M_writer('\n            </div>\n          </div>\n        </div>\n      </header>\n      <div id="main" class="main container">\n        ')
        __M_writer(str(next.body()))
        __M_writer('\n      </div>\n      <button onclick="topFunction()" id="myBtn" title="Go to top"><i class="fa fa-arrow-up"></i></button>\n    </div>\n    <script type="text/javascript">\n      msg = \'\'\n')
        if perm&lazylibrarian.perm_config:
            pass
            if not CONFIG['TELEMETRY_ENABLE']:
                __M_writer('          title = \'LazyLibrarian Telemetry\'\n          msg = \'<div class="input-group">LazyLibrarian has the ability to send basic information about the installation, how it is configured,\'\n          msg += \' and how it is used to a server. This helps the developers figure out where it is worth improving, and which parts nobody uses.\'\n          msg += \' All telemetry information is 100% anonymized.<br><br>\'\n          msg += \'<a href="#" class="btn btn-xs btn-primary" data-toggle="tooltip" title="Enable Telemetry" id="enableTelemetry">Turn on</a>&nbsp;\'\n          msg += \'<a href="#" class="btn btn-xs btn-primary" data-toggle="tooltip" title="Ask me again later" id="ignoreTelemetry">Maybe Later</a></div>\'\n          if (readCookie(\'ignoreTelemetry\') != null) { msg = \'\' }\n')
            elif CONFIG['INSTALL_TYPE'] in ['git', 'source']:
                __M_writer("          title = 'LazyLibrarian Update'\n")
                if not CONFIG['CURRENT_VERSION']:
                    __M_writer('              msg = \'<div class="input-group">You are running an unknown version of lazylibrarian\'\n')
                elif (CONFIG['INSTALL_TYPE'] == 'source' and CONFIG['CURRENT_VERSION'] == 'No Version File' ):
                    __M_writer('              msg = \'<div class="input-group">You are running an unknown version via source install\'\n')
                elif CONFIG['CURRENT_VERSION'] != CONFIG['LATEST_VERSION']:
                    pass
                    if CONFIG['LATEST_VERSION'] == 'Not_Available_From_Git':
                        __M_writer('              msg = \'<div class="input-group">Unable to get the latest version from git\'\n')
                    elif CONFIG.get_int('COMMITS_BEHIND') < 0:
                        __M_writer('              msg = \'<div class="input-group">Running a local updated version. Push changes to git or rollback to Master release\'\n')
                    elif CONFIG.get_int('COMMITS_BEHIND') == 1:
                        __M_writer('              msg = \'<div class="input-group">New version available. You are one commit behind.\'\n')
                    elif CONFIG.get_int('COMMITS_BEHIND') > 1:
                        __M_writer('              msg = \'<div class="input-group">New version available. You are ')
                        __M_writer(str(CONFIG['COMMITS_BEHIND']))
                        __M_writer(" commits behind.'\n")
                    if CONFIG.get_int('COMMITS_BEHIND') > 0:
                        pass
                        if "** MANUAL **" in lazylibrarian.COMMIT_LIST:
                            __M_writer("                msg += '<strong>Manual update is required</strong>'\n")
                        __M_writer("              msg += '</div><div>'\n")
                        if "** MANUAL **" not in lazylibrarian.COMMIT_LIST and not docker():
                            __M_writer('                  msg += \'<a href="update" class="btn btn-xs btn-primary" data-toggle="tooltip" title="Update to the latest release" id="doUpdate">Update</a>&nbsp;\'\n')
                        __M_writer('              msg += \'<a href="#" class="btn btn-xs btn-primary" data-toggle="tooltip" title="Show Changes" id="getChangelog">Changes</a>&nbsp;\'\n')
                else:
                    __M_writer("            msg = ''\n")
                __M_writer('          if (msg.length) {\n            msg += \'<a href="#" class="btn btn-xs btn-primary" data-toggle="tooltip" title="Ignore the update message for 24 hours" id="ignoreUpdate">Ignore</a></div>\'\n          }\n          if (readCookie(\'ignoreUpdate\') != null) { msg = \'\' }\n')
        __M_writer('\n      $(document).ready(function() {\n          \n        if (msg != \'\') {\n          $.notify({\n              icon: "images/ll48.png",\n              title: \'<strong>\'+title+\'</strong>\',\n              message: msg\n          },{\n              icon_type: \'image\',\n              type: \'info\',\n              delay: 20000\n            });\n        }\n\n        $(\'#ignoreTelemetry\').click(function() {\n            createCookie("ignoreTelemetry", true, 14);\n            location.reload(true);\n        });\n       $(\'#enableTelemetry\').on(\'click\', function(e) {\n            $.get(\'enable_telemetry\', function(data) {\n                bootbox.dialog({\n                    title: \'Enable Telemetry\',\n                    message: \'<pre>\'+data+\'</pre>\',\n                    buttons: {\n                        primary: {\n                            label: "Close",\n                            className: \'btn-primary\',\n                            callback: function(){ location.reload(true); }\n                        },\n                    }\n                });\n            });\n        });\n\n        $(\'#ignoreUpdate\').click(function() {\n            createCookie("ignoreUpdate", true, 1);\n            location.reload(true);\n        });\n\n        $(\'#doUpdate\').click(function () {\n            createCookie("ignoreUpdate", true, 0.01);  // suppress popup while updating\n            location.reload(true);\n        });\n       $(\'#getChangelog\').on(\'click\', function(e) {\n            $.get(\'check_for_updates\', function(data) {\n                bootbox.dialog({\n                    title: \'Check Version\',\n                    message: \'<pre>\'+data+\'</pre>\',\n                    buttons: {\n                        primary: {\n                            label: "Close",\n                            className: \'btn-primary\',\n                            callback: function(){ location.reload(true); }\n                        },\n                    }\n                });\n            });\n        });\n      });\n\n      // Initialise tooltips\n      $(function () {\n        $(\'[data-toggle="tooltip"]\').tooltip()\n      })\n\n        function truncateOnWord(str, limit) {\n            var trimmable = \'\\u0009\\u000A\\u000B\\u000C\\u000D\\u0020\\u00A0\\u1680\\u180E\\u2000\\u2001\\u2002\\u2003\\u2004\\u2005\\u2006\\u2007\\u2008\\u2009\\u200A\\u202F\\u205F\\u2028\\u2029\\u3000\\uFEFF\';\n            var reg = new RegExp(\'(?=[\' + trimmable + \'])\');\n            var words = str.split(reg);\n            var count = 0;\n            var result = words.filter(function(word) {\n                count += word.length;\n                return count <= limit;\n            }).join(\'\');\n            if (str.length - result.length <= 4) {return str};\n            return result + \' ...\'\n        }\n\n        // When the user scrolls down 20px from the top of the document, show the button\n        window.onscroll = function() {scrollFunction()};\n\n        function scrollFunction() {\n            if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {\n                document.getElementById("myBtn").style.display = "block";\n            } else {\n                document.getElementById("myBtn").style.display = "none";\n            }\n        }\n\n        // When the user clicks on the button, scroll to the top of the document\n        function topFunction() {\n            document.body.scrollTop = 0;\n            document.documentElement.scrollTop = 0;\n        }\n\n      function createCookie(name, value, days) {\n      var expires;\n\n      if (days) {\n          var date = new Date();\n          date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));\n          expires = "; expires=" + date.toGMTString();\n      } else {\n          expires = "";\n      }\n      document.cookie = encodeURIComponent(name) + "=" + encodeURIComponent(value) + expires + "; path=/";\n      }\n\n      function readCookie(name) {\n      var nameEQ = encodeURIComponent(name) + "=";\n      var ca = document.cookie.split(\';\');\n      for (var i = 0; i < ca.length; i++) {\n          var c = ca[i];\n          while (c.charAt(0) === \' \') c = c.substring(1, c.length);\n          if (c.indexOf(nameEQ) === 0) return decodeURIComponent(c.substring(nameEQ.length, c.length));\n      }\n      return null;\n      }\n\n      function eraseCookie(name) {\n      createCookie(name, "", -1);\n      }\n\n      function bookinfo(bookid) {\n        $.get(\'bookdesc\', {\'bookid\': bookid},\n        function(data) {\n            var $textAndPic = $(\'<div></div>\');\n            var res = data.split(\'^\');\n            var img = res[0]\n            var title = res[1]\n            var desc = res[2]\n            $textAndPic.append(\'<img src="./\' + img + \'" class="box-shadow img-responsive" />\');\n            $textAndPic.append(\'<br>\' + desc + \' <br />\');\n            bootbox.dialog({\n                size: "large",\n                title: title,\n                message: $textAndPic,\n                buttons: {\n                   primary: {\n                        label: "Close",\n                        className: \'btn-primary\'\n                    }\n                }\n            })\n        })\n      }\n\n    // Read a page\'s GET URL variables and return them as an associative array.\n    function getUrlVars() {\n        var vars = [], hash;\n        var hashes = window.location.href.slice(window.location.href.indexOf(\'?\') + 1).split(\'&\');\n        for(var i = 0; i < hashes.length; i++) {\n            hash = hashes[i].split(\'=\');\n            vars.push(hash[0]);\n            vars[hash[0]] = hash[1];\n        }\n        return vars;\n    }\n    </script>\n  </body>\n</html>\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascriptIncludes(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_headIncludes(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_headerIncludes(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/app/lazylibrarian/data/interfaces/bookstrap/base.html", "uri": "base.html", "source_encoding": "utf-8", "line_map": {"16": 0, "25": 1, "26": 2, "27": 3, "28": 4, "29": 5, "30": 6, "33": 5, "34": 11, "35": 11, "36": 19, "37": 20, "38": 20, "39": 20, "40": 21, "41": 22, "42": 24, "43": 44, "44": 44, "45": 70, "46": 70, "47": 193, "49": 194, "51": 195, "52": 196, "53": 198, "54": 199, "55": 203, "56": 204, "57": 206, "59": 207, "61": 208, "62": 209, "63": 213, "65": 214, "67": 215, "68": 216, "69": 220, "71": 221, "73": 222, "74": 223, "75": 231, "77": 232, "79": 233, "80": 234, "81": 242, "83": 243, "85": 244, "86": 245, "87": 249, "89": 250, "90": 251, "91": 252, "92": 253, "93": 256, "94": 257, "95": 259, "96": 260, "97": 262, "98": 263, "99": 265, "100": 271, "101": 271, "102": 277, "103": 277, "104": 283, "106": 284, "107": 285, "108": 292, "109": 293, "110": 294, "111": 295, "112": 296, "113": 297, "114": 298, "116": 299, "117": 300, "118": 301, "119": 302, "120": 303, "121": 304, "122": 305, "123": 306, "124": 306, "125": 306, "126": 308, "128": 309, "129": 310, "130": 312, "131": 313, "132": 314, "133": 316, "134": 318, "135": 319, "136": 321, "137": 327, "138": 489, "139": 490, "140": 491, "146": 489, "155": 490, "164": 491, "173": 164}}
__M_END_METADATA
"""
