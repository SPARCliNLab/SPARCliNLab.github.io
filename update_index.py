import re

with open('index.html', 'r') as f:
    content = f.read()

# Find and replace the closing style tag with enhanced CSS
old_style_end = '''        }
    </style>'''

new_style_end = '''        }

        .card-link {
            position: absolute;
            top: 0;
            bottom: 0;
            left: 0;
            width: 100%;
            cursor: pointer;
            font-size: 1.5rem;
            display: flex;
            align-items: flex-start;
            justify-content: flex-end;
            padding: 10px;
            color: #1e3a8a;
            opacity: 1;
            transition: opacity 0.2s ease;
        }

        .card:hover .card-link {
            opacity: 1;
        }

        #publications a {
            text-decoration: underline;
            color: #1e3a8a;
        }

        #publications a:hover {
            color: #4f46e5;
        }
    </style>'''

# Replace only the final one (look for card tag before it)
pattern = r'(        \}\n\n        /\* clickable card link \*/\n        \pattern = r'(        \}\n\n      on: absolute;\n           pattern = r'(        \}\n\n        /\* cl     left: 0;\n   pattern = r'(     0%;\n      pattern = r'style>)'

replacement = r'''\1

                   {
                              ;
                  ;
                  : 0;
                  0;
                                     cursor: pointer;
            font-size: 1.5rem;
                       ex;
                                                                         d;
                     10px;
                                        opacity: 1;
                                                              .card:hover .card-link {
            opacity: 1;
        }

                                                                                            ;
                   #publications a:hover {
            color: #4f46e5;
        }
    </style>'''

content = content.replace('        /* clickable card link */\ncontent = content.replace('        /* clickable card link */\ncontent = content.replace('        /* clickable card link */\ncontent = content.replace('        /* clickable card link */\ncontent = content.replace('        /* clickable card    content = content.re;
content = content.r
                     ;
            left: 0;
                                                   r;                                                   r flex;
            align-items: flex-start;
            justify-content: flex-end;
            padding: 10px;
            color: #1e3a8a;
            opacity: 1;
                                                   }

        .card:hover .card-link {
            opacity: 1;
        }

        #publications a {
            text-decoration: underline;
            color: #1e3a8a;
        }

        #publications a:hover {
                                                 >'''                         , '        :
            content)

print("Successfully updated CSS")
