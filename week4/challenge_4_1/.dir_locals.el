;;; .dir_locals.el --- Description -*- lexical-binding: t; -*-
;;
;; Copyright (C) 2022 Ethan Goan
;;
;; Author: Ethan Goan <ethanjgoan@gmail.com>
;; Maintainer: Ethan Goan <ethanjgoan@gmail.com>
;; Created: July 03, 2022
;; Modified: July 03, 2022
;; Version: 0.0.1
;; Keywords: abbrev bib c calendar comm convenience data docs emulations extensions faces files frames games hardware help hypermedia i18n internal languages lisp local maint mail matching mouse multimedia news outlines processes terminals tex tools unix vc wp
;; Homepage: https://github.com/ethan/.dir_locals
;; Package-Requires: ((emacs "24.3"))
;;
;; This file is not part of GNU Emacs.
;;
;;; Commentary:
;;
;;  Description
;;
;;; Code:
((nil (org-format-latex-header . "\\documentclass{/home/ethan/Documents/uai2022/bmaw2022}\n\\usepackage{xcolor}\n\\definecolor{background_colour}{HTML}{1E1D2F}\n\\definecolor{text_colour}{HTML}{F5C2E7}\n\\pagecolor{background_colour}\n\\color{text_colour}\n[PACKAGES]\n[DEFAULT-PACKAGES]\n\\pagestyle{empty}             % do not remove\n% The settings below are copied from fullpage.sty\n\\setlength{\\textwidth}{\\paperwidth}\n\\addtolength{\\textwidth}{-3cm}\n\\setlength{\\oddsidemargin}{1.5cm}\n\\addtolength{\\oddsidemargin}{-2.54cm}\n\\setlength{\\evensidemargin}{\\oddsidemargin}\n\\setlength{\\textheight}{\\paperheight}\n\\addtolength{\\textheight}{-\\headheight}\n\\addtolength{\\textheight}{-\\headsep}\n\\addtolength{\\textheight}{-\\footskip}\n\\addtolength{\\textheight}{-3cm}\n\\setlength{\\topmargin}{1.5cm}\n\\addtolength{\\topmargin}{-2.54cm}")))
(provide '.dir_locals)
