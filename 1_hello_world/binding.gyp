{
    "targets": [
        {
            "target_name": "addon",
            "cflags!": ["-fno-exceptions"],
            "cflags_cc!": ["-fno-exceptions"],
            "sources": [
              "node-addon-api/person/Person.c",
              "node-addon-api/person/Person.h",
              "hello.cc"
              ],
            "include_dirs": [
                "<!@(node -p \"require('node-addon-api').include\")",
                # "quotation",
                # "quotation/basic",
                # "quotation/basic/investmentLink",
                # "quotation/basic/traditional",
                # "quotation/basic/traditional/term",
                # "quotation/basic/universalLife",
                # "quotation/shared",
            ],
            "defines": ["NAPI_DISABLE_CPP_EXCEPTIONS"],
        }
    ]
}
