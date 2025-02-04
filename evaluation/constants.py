import numpy as np

CONALA_CV_SUBSETS = np.array(
        [[224, 421, 392, 380, 414, 437,  76,  20,   2, 174, 240, 355, 303,
        230, 326, 328, 233, 116, 340, 291, 425, 186,  24,  46,  74,  81,
        283,  58, 360,   4, 246, 465, 356, 217, 431,  25, 214, 169, 238,
        412, 390, 204, 144, 409, 191,  69,  37, 279, 298, 407,  29, 118,
         88, 222, 314,  90, 466, 251, 415,  23,  22, 450, 158, 363, 145,
        227, 387, 454, 128, 180,  15, 249, 268, 396, 339, 468, 234,   6,
        252, 402, 197,  42, 167, 153, 143,  63,  71, 470,   1, 105, 388,
        209,  36, 416, 208, 205, 138, 275, 460, 400],
       [310, 293, 371,  40, 351, 111, 117, 270, 177, 253, 420, 407,  53,
        327, 462,  65, 402, 334, 262, 453, 119,  58, 468, 410, 143, 190,
        455, 221,   1, 386,   5, 367, 118, 286, 281, 174, 242, 209, 102,
        461, 247,  39,  94, 291,  20,  84, 460, 439, 136, 113, 294, 343,
        122, 133, 194, 175, 256, 359, 218,  35, 171, 305, 135, 274, 436,
         85,  92,  30, 414,   2, 165, 240, 107, 466, 184, 295, 248, 325,
        257, 358, 199,  64, 347, 403,  71, 182, 428, 316, 418,  11, 114,
        396, 148, 352, 196, 160,  15, 112,  79, 388],
       [ 63, 233, 401, 408, 330,  34, 454,  55, 108, 160, 351, 282, 464,
        176, 370, 347,  15,  72, 204,  58, 430, 139, 349,  42,   6, 281,
         92, 168, 298,  24,  66, 127, 422, 210, 207, 447, 357, 405, 318,
        335, 448, 128, 470, 208,  85, 388, 163,  36, 200, 166, 425, 167,
        371,  54, 355, 239, 416, 201, 194, 383, 364, 135, 348, 248, 468,
         62, 258, 376, 363, 246, 222, 152, 377,  90, 287, 263, 186,  53,
          3, 265, 217,   5, 235, 254, 427, 164, 456, 155, 197, 395, 467,
        378,  30, 226, 399, 440,  81, 134, 404, 129],
       [ 76, 223, 354, 263, 216,  12, 141, 217, 215, 229,  97, 121, 108,
        277, 292, 436, 471, 240, 391, 400, 337, 470,  32, 455, 244,  91,
        316,  59, 281, 266, 225, 325, 234,  24, 178,  81, 434,   9, 386,
        142,  27, 309, 460, 154, 371,  38, 387,  52, 122, 248,  22, 358,
         90, 427, 433, 274,  11,  53, 161, 247, 306, 440, 294, 190, 210,
        381,  98, 446, 453, 242, 273, 160, 331, 383,  25, 363, 195,   3,
        334, 459,  10, 438,  28, 441, 435, 416, 405, 347,  37, 171,  34,
        404, 196,   6, 445, 268, 328, 115, 299, 428],
       [ 59, 250, 223, 346, 276, 174, 456, 329, 248,   9, 277,  87, 469,
        240,  75, 366, 438, 190, 404, 460,  26, 191, 176, 459,  48, 253,
        140, 260, 116, 308, 219,  84, 279, 228,   2,  61, 352, 338, 120,
        181,  12, 117, 359, 373,   1, 369, 209,  47, 106, 415, 334,  86,
        158, 315, 156, 448, 133, 398, 303, 203, 342,  74, 189, 358, 392,
         95, 247,  32, 171, 399, 319, 381, 333, 374,  97, 417,  54, 211,
        332, 271, 431, 125, 244,  51, 165, 437,  25, 385, 275, 286,  45,
         98, 169, 406, 264, 297, 114,  10, 314, 430]])

HUMANEVAL_CV_SUBSETS = np.array(
       [[  4,  28, 127,  78,  72,  13, 157,  94, 139, 133,  86, 122,   9,
         50, 121,  10,   6,  35, 145,  69,  52,  38,  36, 144, 128, 119,
          7,  37,  20,  47],
       [ 23, 124,  40,  36,  31,   2,  25,  94, 123, 113,  33, 141, 108,
         61, 128, 160,  11,  15,  83, 129, 127, 135,   0, 156,  18,  66,
         44,  90,  54, 154],
       [110, 150,  26,   2, 128,  74,  25,  31,  57, 137,  56,  20, 136,
        140,  93,  24,  43,  71,  92,  12,   9,  22, 157, 119, 134, 120,
        135, 111,  65,  33],
       [  6,  97, 137, 139,  59,  75,  91,  39,   4, 113,  52,  99,  56,
        142,  57, 121,  29,  80, 109,  98,  53,  37,  49,  33,  31,  94,
        123, 147,  77, 125],
       [ 59,  47,   4,  75,  10,  40,  33,   5, 155, 154,  35, 116,  26,
         14,  63, 121, 134,  19, 159,  41,   0, 135,  84,  23, 150,  55,
         77, 133,  89,  95]])

MODELS_CONALA = ['baseline', 'tranx-annot', 'best-tranx', 'best-tranx-rerank', 'codex']
MODELS_HUMANEVAL = [str(i) for i in range(200)]