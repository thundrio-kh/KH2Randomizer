from locationClass import *
from itemClass import itemTypes

treasureList = [
    KH2Treasure(245, "Bamboo Grove Dark Shard", locationTypes=["LoD"]),
    KH2Treasure(497, "Bamboo Grove Ether", locationTypes=["LoD"]),
    KH2Treasure(498, "Bamboo Grove Mythril Shard", locationTypes=["LoD"]),
    KH2Treasure(21, "Checkpoint Hi-Potion", locationTypes=["LoD"]),
    KH2Treasure(121, "Checkpoint Mythril Shard", locationTypes=["LoD"]),
    KH2Treasure(22, "Mountain Trail Lightning Shard", locationTypes=["LoD"]),
    KH2Treasure(23, "Mountain Trail Recovery Recipe", locationTypes=["LoD"]),
    KH2Treasure(122, "Mountain Trail Ether", locationTypes=["LoD"]),
    KH2Treasure(123, "Mountain Trail Mythril Shard", locationTypes=["LoD"]),
    KH2Treasure(124, "Village Cave AP Boost", locationTypes=["LoD"]),
    KH2Treasure(125, "Village Cave Dark Shard", locationTypes=["LoD"]),
    KH2Treasure(24, "Ridge Frost Shard", locationTypes=["LoD"]),
    KH2Treasure(126, "Ridge AP Boost", locationTypes=["LoD"]),
    KH2Treasure(25, "Throne Room Torn Pages", locationTypes=["LoD"]),
    KH2Treasure(127, "Throne Room Palace Map", locationTypes=["LoD"]),
    KH2Treasure(26, "Throne Room AP Boost", locationTypes=["LoD"]),
    KH2Treasure(27, "Throne Room Queen Recipe", locationTypes=["LoD"]),
    KH2Treasure(128, "Throne Room AP Boost", locationTypes=["LoD"]),
    KH2Treasure(129, "Throne Room Ogre Shield", locationTypes=["LoD"]),
    KH2Treasure(130, "Throne Room Mythril Crystal", locationTypes=["LoD"]),
    KH2Treasure(131, "Throne Room Orichalcum", locationTypes=["LoD"]),

    KH2Treasure(28, "Agrabah Dark Shard", locationTypes=["Agrabah"]),
    KH2Treasure(29, "Agrabah Mythril Shard", locationTypes=["Agrabah"]),
    KH2Treasure(30, "Agrabah Hi-Potion", locationTypes=["Agrabah"]),
    KH2Treasure(132, "Agrabah AP Boost", locationTypes=["Agrabah"]),
    KH2Treasure(133, "Agrabah Mythril Stone", locationTypes=["Agrabah"]),
    KH2Treasure(249, "Agrabah Mythril Shard", locationTypes=["Agrabah"]),
    KH2Treasure(501, "Agrabah Serenity Shard", locationTypes=["Agrabah"]),
    KH2Treasure(31, "Bazaar Mythril Gem", locationTypes=["Agrabah"]),
    KH2Treasure(32, "Bazaar Power Shard", locationTypes=["Agrabah"]),
    KH2Treasure(33, "Bazaar Hi-Potion", locationTypes=["Agrabah"]),
    KH2Treasure(134, "Bazaar AP Boost", locationTypes=["Agrabah"]),
    KH2Treasure(135, "Bazaar Mythril Shard", locationTypes=["Agrabah"]),
    KH2Treasure(136, "Palace Walls Skill Ring", locationTypes=["Agrabah"]),
    KH2Treasure(520, "Palace Walls Mythril Stone", locationTypes=["Agrabah"]),
    KH2Treasure(250, "Entrance Power Stone", locationTypes=["Agrabah"]),
    KH2Treasure(251, "Entrance Mythril Shard", locationTypes=["Agrabah"]),
    KH2Treasure(35, "Valley of Stone Mythril Stone", locationTypes=["Agrabah"]),
    KH2Treasure(36, "Valley of Stone AP Boost", locationTypes=["Agrabah"]),
    KH2Treasure(137, "Valley of Stone Mythril Shard", locationTypes=["Agrabah"]),
    KH2Treasure(138, "Valley of Stone Hi-Potion", locationTypes=["Agrabah"]),
    KH2Treasure(487, "Chasm of Challenges Cave of Wonders Map", locationTypes=["Agrabah"]),
    KH2Treasure(37, "Chasm of Challenges AP Boost", locationTypes=["Agrabah"]),
    KH2Treasure(502, "Treasure Room AP Boost", locationTypes=["Agrabah"]),
    KH2Treasure(503, "Treasure Room Serenity Gem", locationTypes=["Agrabah"]),
    KH2Treasure(34, "Ruined Chamber Torn Pages", locationTypes=["Agrabah"], invalidChecks=["Fire","Blizzard","Thunder"]),
    KH2Treasure(486, "Ruined Chamber Ruins Map", locationTypes=["Agrabah"], invalidChecks=["Fire","Blizzard","Thunder"]),

    KH2Treasure(79, "Cornerstone Hill Cornerstone Hill Map", locationTypes=["DC"]),
    KH2Treasure(12, "Cornerstone Hill Frost Shard", locationTypes=["DC"]),
    KH2Treasure(81, "Pier Mythril Shard", locationTypes=["DC"]),
    KH2Treasure(82, "Pier Hi-Potion", locationTypes=["DC"]),
    KH2Treasure(83, "Waterway Mythril Stone", locationTypes=["DC"]),
    KH2Treasure(84, "Waterway AP Boost", locationTypes=["DC"]),
    KH2Treasure(85, "Waterway Frost Stone", locationTypes=["DC"]),
    KH2Treasure(16, "Courtyard Mythril Shard", locationTypes=["DC"]),
    KH2Treasure(17, "Courtyard Star Recipe", locationTypes=["DC"]),
    KH2Treasure(18, "Courtyard AP Boost", locationTypes=["DC"]),
    KH2Treasure(92, "Courtyard Mythril Stone", locationTypes=["DC"]),
    KH2Treasure(93, "Courtyard Blazing Stone", locationTypes=["DC"]),
    KH2Treasure(247, "Courtyard Blazing Shard", locationTypes=["DC"]),
    KH2Treasure(248, "Courtyard Mythril Shard", locationTypes=["DC"]),
    KH2Treasure(91, "Library Torn Pages", locationTypes=["DC"]),

    KH2Treasure(313, "Pooh Bear's House 100 Acre Wood Map", locationTypes=["100AW"]),
    KH2Treasure(97, "Pooh Bear's House AP Boost", locationTypes=["100AW"]),
    KH2Treasure(98, "Pooh Bear's House Mythril Stone", locationTypes=["100AW"]),
    KH2Treasure(105, "Piglet's House Defense Boost", locationTypes=["100AW"], invalidChecks=["TornPage"]),
    KH2Treasure(103, "Piglet's House AP Boost", locationTypes=["100AW"], invalidChecks=["TornPage"]),
    KH2Treasure(104, "Piglet's House Mythril Gem", locationTypes=["100AW"], invalidChecks=["TornPage"]),
    KH2Treasure(314, "Rabbit's House Draw Ring", locationTypes=["100AW"], invalidChecks=["TornPage"]),
    KH2Treasure(100, "Rabbit's House Mythril Crystal", locationTypes=["100AW"], invalidChecks=["TornPage"]),
    KH2Treasure(101, "Rabbit's House AP Boost", locationTypes=["100AW"], invalidChecks=["TornPage"]),
    KH2Treasure(108, "Kanga's House Magic Boost", locationTypes=["100AW"], invalidChecks=["TornPage"]),
    KH2Treasure(106, "Kanga's House AP Boost", locationTypes=["100AW"], invalidChecks=["TornPage"]),
    KH2Treasure(107, "Kanga's House Orichalcum", locationTypes=["100AW"], invalidChecks=["TornPage"]),
    KH2Treasure(110, "The Spooky Cave Mythril Gem", locationTypes=["100AW"], invalidChecks=["TornPage"]),
    KH2Treasure(111, "The Spooky Cave AP Boost", locationTypes=["100AW"], invalidChecks=["TornPage"]),
    KH2Treasure(112, "The Spooky Cave Orichalcum", locationTypes=["100AW"], invalidChecks=["TornPage"]),
    KH2Treasure(113, "The Spooky Cave Guard Recipe", locationTypes=["100AW"], invalidChecks=["TornPage"]),
    KH2Treasure(115, "The Spooky Cave Mythril Crystal", locationTypes=["100AW"], invalidChecks=["TornPage"]),
    KH2Treasure(116, "The Spooky Cave AP Boost", locationTypes=["100AW"], invalidChecks=["TornPage"]),
    KH2Treasure(312, "Starry Hill Cosmic Ring", locationTypes=["100AW"], invalidChecks=["TornPage"]),
    KH2Treasure(94, "Starry Hill Style Recipe", locationTypes=["100AW"], invalidChecks=["TornPage"]),

    KH2Treasure(242, "Underworld Entrance Power Boost", locationTypes=["OC"]),
    KH2Treasure(7,"Cave of the Dead: Passage Mythril Shard", locationTypes=["OC"]),
    KH2Treasure(8,"Cave of the Dead: Passage Mythril Stone", locationTypes=["OC"]),
    KH2Treasure(144, "Passage Ether", locationTypes=["OC"]),
    KH2Treasure(145, "Passage AP Boost", locationTypes=["OC"]),
    KH2Treasure(146, "Passage Hi-Potion", locationTypes=["OC"]),
    KH2Treasure(2,"Cave of the Dead: Inner Chamber Underworld Map", locationTypes=["OC"]),
    KH2Treasure(243, "Inner Chamber Mythril Shard", locationTypes=["OC"]),
    KH2Treasure(3,"Underworld Caverns: Entrance Lucid Shard", locationTypes=["OC"]),
    KH2Treasure(11, "Entrance AP Boost", locationTypes=["OC"]),
    KH2Treasure(504, "Entrance Mythril Shard", locationTypes=["OC"]),
    KH2Treasure(9,"Underworld Caverns: The Lost Road Bright Shard", locationTypes=["OC"]),
    KH2Treasure(10, "The Lost Road Ether", locationTypes=["OC"]),
    KH2Treasure(148, "The Lost Road Mythril Shard", locationTypes=["OC"]),
    KH2Treasure(149, "The Lost Road Mythril Stone", locationTypes=["OC"]),
    KH2Treasure(150, "Atrium Lucid Stone", locationTypes=["OC"]),
    KH2Treasure(151, "Atrium AP Boost", locationTypes=["OC"]),
    KH2Treasure(244, "The Lock Caverns Map", locationTypes=["OC"]),
    KH2Treasure(5,"The Lock Mythril Shard", locationTypes=["OC"]),
    KH2Treasure(142, "The Lock AP Boost", locationTypes=["OC"]),

    KH2Treasure(39, "Courtyard AP Boost", locationTypes=["BC"]),
    KH2Treasure(40, "Courtyard Hi-Potion", locationTypes=["BC"]),
    KH2Treasure(505, "Courtyard Mythril Shard", locationTypes=["BC"]),
    KH2Treasure(46, "Belle's Room Castle Map", locationTypes=["BC"]),
    KH2Treasure(240, "Belle's Room Mega-Recipe", locationTypes=["BC"]),
    KH2Treasure(63, "The East Wing Mythril Shard", locationTypes=["BC"]),
    KH2Treasure(155, "The East Wing Tent", locationTypes=["BC"]),
    KH2Treasure(41, "The West Hall Hi-Potion", locationTypes=["BC"]),
    KH2Treasure(206, "The West Hall Mythril Shard", locationTypes=["BC"]),
    KH2Treasure(207, "The West Hall Power Shard", locationTypes=["BC"]),
    KH2Treasure(208, "The West Hall Mythril Shard", locationTypes=["BC"]),
    KH2Treasure(158, "The West Hall AP Boost", locationTypes=["BC"]),
    KH2Treasure(159, "The West Hall Bright Stone", locationTypes=["BC"]),
    KH2Treasure(239, "Dungeon Basement Map", locationTypes=["BC"]),
    KH2Treasure(43, "Dungeon AP Boost", locationTypes=["BC"]),
    KH2Treasure(44, "Secret Passage Mythril Shard", locationTypes=["BC"]),
    KH2Treasure(168, "Secret Passage Hi-Potion", locationTypes=["BC"]),
    KH2Treasure(45, "Secret Passage Lucid Shard", locationTypes=["BC"]),
    KH2Treasure(42, "The West Wing Mythril Shard", locationTypes=["BC"]),
    KH2Treasure(164, "The West Wing Tent", locationTypes=["BC"]),
    KH2Treasure(241, "The Beast's Room Blazing Shard", locationTypes=["BC"]),

    KH2Treasure(316, "00 Pit Cell Area Map", locationTypes=["SP"]),
    KH2Treasure(64, "00 Mythril Crystal", locationTypes=["SP"]),
    KH2Treasure(65, "01 Dark Crystal", locationTypes=["SP"]),
    KH2Treasure(171, "01 Mythril Stone", locationTypes=["SP"]),
    KH2Treasure(253, "01 Mythril Gem", locationTypes=["SP"]),
    KH2Treasure(521, "01 Frost Crystal", locationTypes=["SP"]),
    KH2Treasure(49, "04 Power Crystal", locationTypes=["SP"]),
    KH2Treasure(50, "04 AP Boost", locationTypes=["SP"]),
    KH2Treasure(255, "05 I/O Tower Map", locationTypes=["SP"]),
    KH2Treasure(499, "05 Gaia Belt", locationTypes=["SP"]),
    KH2Treasure(177, "08 AP Boost", locationTypes=["SP"]),
    KH2Treasure(178, "08 Orichalcum+", locationTypes=["SP"]),
    KH2Treasure(51, "08 Cosmic Arts", locationTypes=["SP"]),
    KH2Treasure(488, "08 Central Computer Core Map", locationTypes=["SP"]),

    KH2Treasure(53, "02 Mythril Shard", locationTypes=["HT"]),
    KH2Treasure(212, "02 Serenity Gem", locationTypes=["HT"]),
    KH2Treasure(211, "01 Halloween Town Map", locationTypes=["HT"]),
    KH2Treasure(209, "00 Mythril Stone", locationTypes=["HT"]),
    KH2Treasure(210, "00 Energy Shard", locationTypes=["HT"]),
    KH2Treasure(54, "04 Lightning Shard", locationTypes=["HT"]),
    KH2Treasure(213, "04 Mythril Stone", locationTypes=["HT"]),
    KH2Treasure(214, "04 AP Boost", locationTypes=["HT"]),
    KH2Treasure(55, "06 Mega-Potion", locationTypes=["HT"]),
    KH2Treasure(56, "06 Mythril Gem", locationTypes=["HT"]),
    KH2Treasure(216, "06 Lightning Stone", locationTypes=["HT"]),
    KH2Treasure(217, "06 Mythril Stone", locationTypes=["HT"]),
    KH2Treasure(57, "08 Christmas Town Map", locationTypes=["HT"]),
    KH2Treasure(58, "08 AP Boost", locationTypes=["HT"]),

    KH2Treasure(70, "00 Naval Map", locationTypes=["PR"]),
    KH2Treasure(219, "00 Mythril Stone", locationTypes=["PR"]),
    KH2Treasure(220, "00 Dark Shard", locationTypes=["PR"]),
    KH2Treasure(71, "02 Dark Stone", locationTypes=["PR"]),
    KH2Treasure(72, "02 AP Boost", locationTypes=["PR"]),
    KH2Treasure(73, "02 Mythril Shard", locationTypes=["PR"]),
    KH2Treasure(221, "02 Mythril Gem", locationTypes=["PR"]),
    KH2Treasure(74, "09 Bright Shard", locationTypes=["PR"]),
    KH2Treasure(223, "09 Mythril Shard", locationTypes=["PR"]),
    KH2Treasure(369, "12 AP Boost", locationTypes=["PR"]),
    KH2Treasure(370, "12 AP Boost", locationTypes=["PR"]),
    KH2Treasure(75, "13 Mythril Shard", locationTypes=["PR"]),
    KH2Treasure(224, "13 Serenity Gem", locationTypes=["PR"]),
    KH2Treasure(371, "13 Power Stone", locationTypes=["PR"]),
    KH2Treasure(252, "11 Feather Charm", locationTypes=["PR"]),
    KH2Treasure(76, "14 AP Boost", locationTypes=["PR"]),
    KH2Treasure(225, "14 Orichalcum", locationTypes=["PR"]),
    KH2Treasure(372, "14 Meteor Staff", locationTypes=["PR"]),
    KH2Treasure(77, "15 Serenity Gem", locationTypes=["PR"]),
    KH2Treasure(78, "15 King Recipe", locationTypes=["PR"]),
    KH2Treasure(373, "15 Mythril Crystal", locationTypes=["PR"]),

    KH2Treasure(194, "09 Drive Recovery", locationTypes=["HB"]),
    KH2Treasure(195, "09 AP Boost", locationTypes=["HB"]),
    KH2Treasure(196, "09 Hi-Potion", locationTypes=["HB"]),
    KH2Treasure(305, "09 Mythril Shard", locationTypes=["HB"]),
    KH2Treasure(506, "09 Dark Shard", locationTypes=["HB"]),
    KH2Treasure(310, "06 Castle Perimeter Map", locationTypes=["HB"]),
    KH2Treasure(189, "06 Mythril Gem", locationTypes=["HB"]),
    KH2Treasure(190, "06 AP Boost", locationTypes=["HB"]),
    KH2Treasure(200, "11 Mythril Stone", locationTypes=["HB"]),
    KH2Treasure(201, "11 Mythril Crystal", locationTypes=["HB"]),
    KH2Treasure(202, "11 Dark Crystal", locationTypes=["HB"]),
    KH2Treasure(307, "11 AP Boost", locationTypes=["HB"]),
    KH2Treasure(184, "05 Skill Recipe", locationTypes=["HB"]),
    KH2Treasure(183, "05 Ukulele Charm", locationTypes=["HB"]),
    KH2Treasure(309, "18 Moon Recipe", locationTypes=["HB"]),
    KH2Treasure(507, "18 AP Boost", locationTypes=["HB"]),
    KH2Treasure(179, "03 Torn Pages", locationTypes=["HB"]),
    KH2Treasure(489, "03 The Great Maw Map", locationTypes=["HB"]),
    KH2Treasure(180, "03 Energy Crystal", locationTypes=["HB"]),
    KH2Treasure(181, "03 AP Boost", locationTypes=["HB"]),
    KH2Treasure(491, "06 Gull Wing", locationTypes=["HB"]),
    KH2Treasure(311, "12 Cosmic Chain", locationTypes=["HB"]),

    KH2Treasure(492, "06 Savannah Map", locationTypes=["PL"]),
    KH2Treasure(404, "06 Dark Gem", locationTypes=["PL"]),
    KH2Treasure(405, "06 Mythril Stone", locationTypes=["PL"]),
    KH2Treasure(401, "05 Frost Gem", locationTypes=["PL"]),
    KH2Treasure(402, "05 Mythril Stone", locationTypes=["PL"]),
    KH2Treasure(403, "05 Bright Stone", locationTypes=["PL"]),
    KH2Treasure(508, "05 AP Boost", locationTypes=["PL"]),
    KH2Treasure(509, "05 Mythril Shard", locationTypes=["PL"]),
    KH2Treasure(418, "00 Pride Rock Map", locationTypes=["PL"]),
    KH2Treasure(392, "00 Mythril Stone", locationTypes=["PL"]),
    KH2Treasure(393, "00 Serenity Crystal", locationTypes=["PL"]),
    KH2Treasure(396, "03 Energy Stone", locationTypes=["PL"]),
    KH2Treasure(397, "03 AP Boost", locationTypes=["PL"]),
    KH2Treasure(398, "03 Mythril Gem", locationTypes=["PL"]),
    KH2Treasure(399, "03 Mythril Stone", locationTypes=["PL"]),
    KH2Treasure(400, "03 Lucid Gem", locationTypes=["PL"]),
    KH2Treasure(406, "07 Mythril Shard", locationTypes=["PL"]),
    KH2Treasure(407, "07 Serenity Gem", locationTypes=["PL"]),
    KH2Treasure(408, "07 Mythril Stone", locationTypes=["PL"]),
    KH2Treasure(409, "08 Serenity Gem", locationTypes=["PL"]),
    KH2Treasure(410, "08 Mythril Stone", locationTypes=["PL"]),
    KH2Treasure(411, "08 Serenity Crystal", locationTypes=["PL"]),
    KH2Treasure(412, "09 Oasis Map", locationTypes=["PL"]),
    KH2Treasure(493, "09 Torn Pages", locationTypes=["PL"]),
    KH2Treasure(413, "09 AP Boost", locationTypes=["PL"]),

    KH2Treasure(315, "32 Potion", locationTypes=["STT"]),
    KH2Treasure(472, "33 Potion", locationTypes=["STT"]),
    KH2Treasure(428, "09 Potion", locationTypes=["STT"]),
    KH2Treasure(429, "09 Hi-Potion", locationTypes=["STT"]),
    KH2Treasure(430, "09 Potion", locationTypes=["STT"]),
    KH2Treasure(434, "10 Ability Ring", locationTypes=["STT"]),
    KH2Treasure(435, "10 Hi-Potion", locationTypes=["STT"]),
    KH2Treasure(436, "10 Potion", locationTypes=["STT"]),
    KH2Treasure(437, "10 Potion", locationTypes=["STT"]),
    KH2Treasure(449, "15 Hi-Potion", locationTypes=["STT"]),
    KH2Treasure(450, "15 Potion", locationTypes=["STT"]),
    KH2Treasure(451, "15 Potion", locationTypes=["STT"]),
    KH2Treasure(455, "16 Elven Bandanna", locationTypes=["STT"]),
    KH2Treasure(456, "16 Potion", locationTypes=["STT"]),
    KH2Treasure(459, "17 Hi-Potion", locationTypes=["STT"]),
    KH2Treasure(463, "22 Hi-Potion", locationTypes=["STT"]),
    KH2Treasure(447, "14 Potion", locationTypes=["TT"]),
    KH2Treasure(448, "14 Mythril Shard", locationTypes=["TT"]),
    KH2Treasure(442, "13 Potion", locationTypes=["TT"]),
    KH2Treasure(443, "13 Mythril Shard", locationTypes=["TT"]),
    KH2Treasure(444, "13 Hi-Potion", locationTypes=["TT"]),
    KH2Treasure(420, "07 Hi-Potion", locationTypes=["TT"]),
    KH2Treasure(421, "07 AP Boost", locationTypes=["TT"]),
    KH2Treasure(422, "07 Tent", locationTypes=["TT"]),
    KH2Treasure(423, "07 Mythril Shard", locationTypes=["TT"]),
    KH2Treasure(424, "07 Potion", locationTypes=["TT"]),
    KH2Treasure(425, "07 Mythril Shard", locationTypes=["TT"]),
    KH2Treasure(484, "07 Potion", locationTypes=["TT"]),
    KH2Treasure(431, "09 Tent", locationTypes=["TT"]),
    KH2Treasure(432, "09 Hi-Potion", locationTypes=["TT"]),
    KH2Treasure(433, "09 Mythril Shard", locationTypes=["TT"]),
    KH2Treasure(465, "25 Potion", locationTypes=["TT"]),
    KH2Treasure(466, "25 Hi-Potion", locationTypes=["TT"]),
    KH2Treasure(522, "25 Ether", locationTypes=["TT"]),
    KH2Treasure(467, "26 Ether", locationTypes=["TT"]),
    KH2Treasure(468, "26 Mythril Shard", locationTypes=["TT"]),
    KH2Treasure(469, "27 Tower Map", locationTypes=["TT"]),
    KH2Treasure(470, "28 Mythril Stone", locationTypes=["TT"]),
    KH2Treasure(479, "37 Mythril Gem", locationTypes=["TT"]),
    KH2Treasure(480, "37 Orichalcum", locationTypes=["TT"]),
    KH2Treasure(481, "37 AP Boost", locationTypes=["TT"]),
    KH2Treasure(482, "37 Mythril Crystal", locationTypes=["TT"]),
    KH2Treasure(477, "36 Orichalcum", locationTypes=["TT"]),
    KH2Treasure(478, "36 Mythril Crystal", locationTypes=["TT"]),
    KH2Treasure(438, "10 Orichalcum+", locationTypes=["TT"]),
    KH2Treasure(439, "10 Mythril Shard", locationTypes=["TT"]),
    KH2Treasure(440, "10 Mythril Crystal", locationTypes=["TT"]),
    KH2Treasure(441, "10 AP Boost", locationTypes=["TT"]),
    KH2Treasure(452, "15 Mythril Crystal", locationTypes=["TT"]),
    KH2Treasure(453, "15 Mythril Stone", locationTypes=["TT"]),
    KH2Treasure(454, "15 Serenity Crystal", locationTypes=["TT"]),
    KH2Treasure(457, "16 Mythril Crystal", locationTypes=["TT"]),
    KH2Treasure(458, "16 Mythril Stone", locationTypes=["TT"]),
    KH2Treasure(460, "17 Orichalcum", locationTypes=["TT"]),
    KH2Treasure(464, "22 Ultimate Recipe", locationTypes=["TT"]),

    KH2Treasure(374, "02 Mythril Stone", locationTypes=["TWTNW"]),
    KH2Treasure(375, "02 Mythril Crystal", locationTypes=["TWTNW"]),
    KH2Treasure(376, "02 AP Boost", locationTypes=["TWTNW"]),
    KH2Treasure(377, "02 Orichalcum", locationTypes=["TWTNW"]),
    KH2Treasure(391, "03 Mythril Crystal", locationTypes=["TWTNW"]),
    KH2Treasure(523, "03 AP Boost", locationTypes=["TWTNW"]),
    KH2Treasure(524, "03 Mythril Stone", locationTypes=["TWTNW"]),
    KH2Treasure(335, "04 Dark City Map", locationTypes=["TWTNW"]),
    KH2Treasure(500, "04 Orichalcum+", locationTypes=["TWTNW"]),
    KH2Treasure(378, "06 Mythril Gem", locationTypes=["TWTNW"]),
    KH2Treasure(379, "06 Orichalcum", locationTypes=["TWTNW"]),
    KH2Treasure(336, "09 Cosmic Belt", locationTypes=["TWTNW"]),
    KH2Treasure(380, "12 Mythril Gem", locationTypes=["TWTNW"]),
    KH2Treasure(381, "12 Orichalcum", locationTypes=["TWTNW"]),
    KH2Treasure(382, "12 Mythril Crystal", locationTypes=["TWTNW"]),
    KH2Treasure(385, "17 Mythril Stone", locationTypes=["TWTNW"]),
    KH2Treasure(386, "17 AP Boost", locationTypes=["TWTNW"]),
    KH2Treasure(387, "17 Mythril Crystal", locationTypes=["TWTNW"]),
    KH2Treasure(388, "17 Orichalcum", locationTypes=["TWTNW"]),

    KH2Treasure(562, "21 AP Boost", locationTypes=["CoR"], invalidChecks=["Form","GrowthAbility"]),
    KH2Treasure(563, "21 Power Crystal", locationTypes=["CoR"], invalidChecks=["Form","GrowthAbility"]),
    KH2Treasure(564, "21 Frost Crystal", locationTypes=["CoR"], invalidChecks=["Form","GrowthAbility"]),
    KH2Treasure(565, "21 Manifest Illusion", locationTypes=["CoR"], invalidChecks=["Form","GrowthAbility"]),
    KH2Treasure(566, "21 AP Boost", locationTypes=["CoR"], invalidChecks=["Form","GrowthAbility"]),
    KH2Treasure(567, "Remembrance Gem", locationTypes=["CoR"], invalidChecks=["Form","GrowthAbility"]),
    KH2Treasure(568, "22 Serenity Gem", locationTypes=["CoR"], invalidChecks=["Form","GrowthAbility"]),
    KH2Treasure(569, "22 AP Boost", locationTypes=["CoR"], invalidChecks=["Form","GrowthAbility"]),
    KH2Treasure(570, "22 Serenity Crystal", locationTypes=["CoR"], invalidChecks=["Form","GrowthAbility"]),
    KH2Treasure(571, "22 Manifest Illusion", locationTypes=["CoR"], invalidChecks=["Form","GrowthAbility"]),
    KH2Treasure(572, "22 Serenity Gem", locationTypes=["CoR"], invalidChecks=["Form","GrowthAbility"]),
    KH2Treasure(573, "22 Dark Remembrance Map", locationTypes=["CoR"], invalidChecks=["Form","GrowthAbility"]),
    KH2Treasure(574, "23 Serenity Crystal", locationTypes=["CoR"], invalidChecks=["Form","GrowthAbility"]),
    KH2Treasure(575, "Remembrance Crystal", locationTypes=["CoR"], invalidChecks=["Form","GrowthAbility"]),
    KH2Treasure(576, "23 AP Boost", locationTypes=["CoR"], invalidChecks=["Form","GrowthAbility"]),
    KH2Treasure(577, "23 Manifest Illusion", locationTypes=["CoR"], invalidChecks=["Form","GrowthAbility"]),
    KH2Treasure(578, "24 AP Boost", locationTypes=["CoR"], invalidChecks=["Form","GrowthAbility"]),
    KH2Treasure(579, "24 AP Boost", locationTypes=["CoR"], invalidChecks=["Form","GrowthAbility"]),
    KH2Treasure(580, "24 Depths of Remembrance Map", locationTypes=["CoR"], invalidChecks=["Form","GrowthAbility"]),
    KH2Treasure(581, "24 Power Boost", locationTypes=["CoR"], invalidChecks=["Form","GrowthAbility"]),
    KH2Treasure(582, "24 Magic Boost", locationTypes=["CoR"], invalidChecks=["Form","GrowthAbility"]),
    KH2Treasure(585, "26 Garden of Assemblage Map", locationTypes=["Free"]),
    KH2Treasure(586, "26 Lost Illusion", locationTypes=["Free"]),
    KH2Treasure(590, "Proof of Nonexistence", locationTypes=["Free"]),

    KH2Treasure(288, "00 Munny Pouch", locationTypes=["STT"]),
    KH2Treasure(389, "00 Champion Belt", locationTypes=["STT"], invalidChecks=itemTypes),
    KH2Treasure(390, "00 Medal", locationTypes=["STT"], invalidChecks=itemTypes),
    KH2Treasure(519, "The Struggle Trophy", locationTypes=["STT"]),
    KH2Treasure(319, "00 Twilight Town Map", locationTypes=["STT"]),
    KH2Treasure(289, "00 Naminé´s Sketches", locationTypes=["STT"]),
    KH2Treasure(483, "00 Mansion Map", locationTypes=["STT"]),

    KH2Treasure(290, "00 Munny Pouch", locationTypes=["TT"]),
    KH2Treasure(291, "00 Crystal Orb", locationTypes=["TT"]),
    KH2Treasure(304, "00 Star Seeker", locationTypes=["TT"]),
    KH2Treasure(286, "00 Valor Form", locationTypes=["TT"]),

    KH2Treasure(362, "00 Marketplace Map", locationTypes=["HB"]),
    KH2Treasure(256, "00 Membership Card", locationTypes=["HB"]),
    KH2Treasure(292, "00 Blizzard Element", locationTypes=["HB"]),

    KH2Treasure(415, "Bamboo Grove Hi-Potion", locationTypes=["LoD"]),
    KH2Treasure(416, "Bamboo Grove Mythril Shard", locationTypes=["LoD"]),
    KH2Treasure(417, "Bamboo Grove AP Boost", locationTypes=["LoD"]),
    KH2Treasure(350, "Bamboo Grove Encampment Area Map", locationTypes=["LoD"]),
    KH2Treasure(495, "Bamboo Grove Village Area Map", locationTypes=["LoD"]),
    KH2Treasure(257, "Bamboo Grove Hidden Dragon", locationTypes=["LoD"]),

    KH2Treasure(299, "00 Cure Element", locationTypes=["BC"]),

    KH2Treasure(258, "00 Baseball Charm", locationTypes=["HB"]),

    KH2Treasure(338, "00 Coliseum Map", locationTypes=["OC"]),
    KH2Treasure(293, "00 Olympus Stone", locationTypes=["OC"]),
    KH2Treasure(260, "00 Hero´s Crest", locationTypes=["OC"]),

    KH2Treasure(261, "Cornerstone Hill Monochrome", locationTypes=["DC"]),

    KH2Treasure(513, "00 Protect Belt", locationTypes=["OC"]),
    KH2Treasure(540, "00 Serenity Gem", locationTypes=["OC"]),

    KH2Treasure(332, "00 Disney Castle Map", locationTypes=["DC"]),
    KH2Treasure(262, "00 Wisdom Form", locationTypes=["DC"]),
    KH2Treasure(368, "Cornerstone Hill Window of Time Map", locationTypes=["DC"]),

    KH2Treasure(329, "00 Isla de Muerta Map", locationTypes=["PR"]),
    KH2Treasure(263, "00 Follow the Wind", locationTypes=["PR"]),

    KH2Treasure(353, "Agrabah Agrabah Map", locationTypes=["Agrabah"]),
    KH2Treasure(300, "Agrabah Lamp Charm", locationTypes=["Agrabah"]),

    KH2Treasure(301, "00 Magnet Element", locationTypes=["HT"]),

    KH2Treasure(264, "00 Circle of Life", locationTypes=["PL"]),
    KH2Treasure(302, "00 Fire Element", locationTypes=["PL"]),

    KH2Treasure(515, "00 Rising Dragon", locationTypes=["OC"]),
    KH2Treasure(542, "00 Serenity Crystal", locationTypes=["OC"]),

    KH2Treasure(294, "00 Seifer´s Trophy", locationTypes=["TT"]),
    KH2Treasure(265, "00 Oathkeeper", locationTypes=["TT"]),
    KH2Treasure(543, "00 Limit Form", locationTypes=["TT"]),

    KH2Treasure(266, "00 Master Form", locationTypes=["HB"]),

    KH2Treasure(267, "00 Photon Debugger", locationTypes=["SP"]),

    KH2Treasure(361, "00 Cure Element", locationTypes=["HB"]),
    KH2Treasure(269, "00 Ice Cream", locationTypes=["HB"]),
    KH2Treasure(511, "00 Picture", locationTypes=["HB"]),

    KH2Treasure(367, "00 Undersea Kingdom Map", locationTypes=["Atlantica"], invalidChecks=["Magnet","Thunder"]),

    KH2Treasure(270, "00 Rumbling Rose", locationTypes=["BC"]),
    KH2Treasure(325, "00 Castle Walls Map", locationTypes=["BC"]),

    KH2Treasure(296, "00 Cursed Medallion", locationTypes=["PR"]),
    KH2Treasure(331, "00 Ship Graveyard Map", locationTypes=["PR"]),

    KH2Treasure(295, "00 Auron´s Statue", locationTypes=["OC"]),
    KH2Treasure(272, "00 Guardian Soul", locationTypes=["OC"]),
    KH2Treasure(514, "00 Genji Shield", locationTypes=["OC"]),
    KH2Treasure(541, "00 Skillful Ring", locationTypes=["OC"]),

    KH2Treasure(303, "Agrabah Wishing Lamp", locationTypes=["Agrabah"], invalidChecks=["Fire","Blizzard","Thunder"]),

    KH2Treasure(297, "00 Present", locationTypes=["HT"]),
    KH2Treasure(298, "00 Decoy Presents", locationTypes=["HT"]),
    KH2Treasure(275, "00 Decisive Pumpkin", locationTypes=["HT"]),

    KH2Treasure(287, "00 Mysterious Abyss", locationTypes=["Atlantica"], invalidChecks=["Magnet","Thunder"]),
    KH2Treasure(279, "00 Blizzard Element", locationTypes=["Atlantica"], invalidChecks=["Magnet","Thunder"]),
    KH2Treasure(538, "00 Orichalcum+", locationTypes=["Atlantica"], invalidChecks=["Magnet","Thunder"]),

    KH2Treasure(284, "00 Sweet Memories", locationTypes=["100AW"], invalidChecks=["TornPage"]),
    KH2Treasure(485, "00 Spooky Cave Map", locationTypes=["100AW"], invalidChecks=["TornPage"]),
    KH2Treasure(285, "00 Cure Element", locationTypes=["100AW"], invalidChecks=["TornPage"]),
    KH2Treasure(539, "00 Orichalcum+", locationTypes=["100AW"], invalidChecks=["TornPage"]),

    KH2Treasure(276, "00 Sleeping Lion", locationTypes=["HB"]),
    KH2Treasure(282, "00 Fenrir", locationTypes=["HB","Sephi"]),

    KH2Treasure(516, "00 Fatal Crest", locationTypes=["OC"]),
    KH2Treasure(517, "00 Orichalcum+", locationTypes=["OC"]),

    KH2Treasure(317, "00 Bond of Flame", locationTypes=["TT"]),

    KH2Treasure(277, "00 Two Become One", locationTypes=["TWTNW"]),
    KH2Treasure(278, "00 Oblivion", locationTypes=["TWTNW"]),
    KH2Treasure(496, "00 Castle That Never Was Map", locationTypes=["TWTNW"]),

    KH2Treasure(518, "00 Hades Cup Trophy", locationTypes=["OC"]),

    KH2Treasure(525, "00 Secret Ansem Report 1", locationTypes=["HB"]),

    KH2Treasure(526, "00 Secret Ansem Report 2", locationTypes=["TT"]),

    KH2Treasure(527, "00 Secret Ansem Report 3", locationTypes=["TWTNW"]),

    KH2Treasure(528, "00 Secret Ansem Report 4", locationTypes=["PR"]),

    KH2Treasure(529, "00 Secret Ansem Report 5", locationTypes=["OC"]),

    KH2Treasure(530, "00 Secret Ansem Report 6", locationTypes=["BC"]),

    KH2Treasure(531, "00 Secret Ansem Report 7", locationTypes=["HB"]),

    KH2Treasure(532, "00 Secret Ansem Report 8", locationTypes=["TWTNW"]),

    KH2Treasure(533, "00 Secret Ansem Report 9", locationTypes=["TWTNW"]),

    KH2Treasure(534, "00 Secret Ansem Report 10", locationTypes=["TT"]),

    KH2Treasure(535, "00 Secret Ansem Report 11", locationTypes=["TWTNW"]),

    KH2Treasure(536, "00 Secret Ansem Report 12", locationTypes=["TWTNW"]),

    KH2Treasure(537, "00 Secret Ansem Report 13", locationTypes=["TWTNW"]),

    KH2Treasure(544, "00 Road to Discovery", locationTypes=["HT","AS"]),

    KH2Treasure(545, "Strength Beyond Strength", locationTypes=["Agrabah","AS"], invalidChecks=["Fire","Blizzard","Thunder"]),

    KH2Treasure(546, "00 Book of Shadows", locationTypes=["OC","AS"]),

    KH2Treasure(547, "00 Cloaked Thunder", locationTypes=["SP","AS"]),

    KH2Treasure(548, "00 Eternal Blossom", locationTypes=["DC","AS"]),

    KH2Treasure(549, "00 Lost Illusion", locationTypes=["HT","AS"]),

    KH2Treasure(550, "00 Lost Illusion", locationTypes=["Agrabah","AS"], invalidChecks=["Fire","Blizzard","Thunder"]),

    KH2Treasure(551, "00 Lost Illusion", locationTypes=["OC","AS"]),

    KH2Treasure(552, "00 Lost Illusion", locationTypes=["SP","AS"]),

    KH2Treasure(553, "00 Lost Illusion", locationTypes=["DC","AS"]),

    KH2Treasure(560, "00 AP Boost", locationTypes=["HB", "DataOrg"]),

    KH2Treasure(559, "00 Defense Boost", locationTypes=["BC","DataOrg"]),

    KH2Treasure(561, "00 Magic Boost", locationTypes=["TT","DataOrg"]),

    KH2Treasure(554, "00 Power Boost", locationTypes=["TWTNW","DataOrg"]),

    KH2Treasure(555, "00 Defense Boost", locationTypes=["LoD", "DataOrg"]),

    KH2Treasure(556, "00 Defense Boost", locationTypes=["PL", "DataOrg"]),

    KH2Treasure(557, "00 AP Boost", locationTypes=["PR", "DataOrg"]),

    KH2Treasure(558, "00 Magic Boost", locationTypes=["STT", "DataOrg"]),

    KH2Treasure(587, "00 Proof of Connection", locationTypes=["DC","LW"], invalidChecks=["ProofofConnection"]),

    KH2Treasure(591, "00 Manifest Illusion", locationTypes=["DC", "LW"], invalidChecks=["ProofofConnection"]),

    KH2Treasure(588, "00 Winner's Proof", locationTypes=["HB"], invalidChecks=["ProofofPeace"]),

    KH2Treasure(589, "00 Proof of Peace", locationTypes=["HB"], invalidChecks=["ProofofPeace"])
]

soraLevelList = [
    KH2LevelUp("Sora", 1),
    KH2LevelUp("Sora", 2),
    KH2LevelUp("Sora", 3),
    KH2LevelUp("Sora", 4),
    KH2LevelUp("Sora", 5),
    KH2LevelUp("Sora", 6),
    KH2LevelUp("Sora", 7),
    KH2LevelUp("Sora", 8),
    KH2LevelUp("Sora", 9),
    KH2LevelUp("Sora", 10),
    KH2LevelUp("Sora", 11),
    KH2LevelUp("Sora", 12),
    KH2LevelUp("Sora", 13),
    KH2LevelUp("Sora", 14),
    KH2LevelUp("Sora", 15),
    KH2LevelUp("Sora", 16),
    KH2LevelUp("Sora", 17),
    KH2LevelUp("Sora", 18),
    KH2LevelUp("Sora", 19),
    KH2LevelUp("Sora", 20),
    KH2LevelUp("Sora", 21),
    KH2LevelUp("Sora", 22),
    KH2LevelUp("Sora", 23),
    KH2LevelUp("Sora", 24),
    KH2LevelUp("Sora", 25),
    KH2LevelUp("Sora", 26),
    KH2LevelUp("Sora", 27),
    KH2LevelUp("Sora", 28),
    KH2LevelUp("Sora", 29),
    KH2LevelUp("Sora", 30),
    KH2LevelUp("Sora", 31),
    KH2LevelUp("Sora", 32),
    KH2LevelUp("Sora", 33),
    KH2LevelUp("Sora", 34),
    KH2LevelUp("Sora", 35),
    KH2LevelUp("Sora", 36),
    KH2LevelUp("Sora", 37),
    KH2LevelUp("Sora", 38),
    KH2LevelUp("Sora", 39),
    KH2LevelUp("Sora", 40),
    KH2LevelUp("Sora", 41),
    KH2LevelUp("Sora", 42),
    KH2LevelUp("Sora", 43),
    KH2LevelUp("Sora", 44),
    KH2LevelUp("Sora", 45),
    KH2LevelUp("Sora", 46),
    KH2LevelUp("Sora", 47),
    KH2LevelUp("Sora", 48),
    KH2LevelUp("Sora", 49),
    KH2LevelUp("Sora", 50),
    KH2LevelUp("Sora", 51),
    KH2LevelUp("Sora", 52),
    KH2LevelUp("Sora", 53),
    KH2LevelUp("Sora", 54),
    KH2LevelUp("Sora", 55),
    KH2LevelUp("Sora", 56),
    KH2LevelUp("Sora", 57),
    KH2LevelUp("Sora", 58),
    KH2LevelUp("Sora", 59),
    KH2LevelUp("Sora", 60),
    KH2LevelUp("Sora", 61),
    KH2LevelUp("Sora", 62),
    KH2LevelUp("Sora", 63),
    KH2LevelUp("Sora", 64),
    KH2LevelUp("Sora", 65),
    KH2LevelUp("Sora", 66),
    KH2LevelUp("Sora", 67),
    KH2LevelUp("Sora", 68),
    KH2LevelUp("Sora", 69),
    KH2LevelUp("Sora", 70),
    KH2LevelUp("Sora", 71),
    KH2LevelUp("Sora", 72),
    KH2LevelUp("Sora", 73),
    KH2LevelUp("Sora", 74),
    KH2LevelUp("Sora", 75),
    KH2LevelUp("Sora", 76),
    KH2LevelUp("Sora", 77),
    KH2LevelUp("Sora", 78),
    KH2LevelUp("Sora", 79),
    KH2LevelUp("Sora", 80),
    KH2LevelUp("Sora", 81),
    KH2LevelUp("Sora", 82),
    KH2LevelUp("Sora", 83),
    KH2LevelUp("Sora", 84),
    KH2LevelUp("Sora", 85),
    KH2LevelUp("Sora", 86),
    KH2LevelUp("Sora", 87),
    KH2LevelUp("Sora", 88),
    KH2LevelUp("Sora", 89),
    KH2LevelUp("Sora", 90),
    KH2LevelUp("Sora", 91),
    KH2LevelUp("Sora", 92),
    KH2LevelUp("Sora", 93),
    KH2LevelUp("Sora", 94),
    KH2LevelUp("Sora", 95),
    KH2LevelUp("Sora", 96),
    KH2LevelUp("Sora", 97),
    KH2LevelUp("Sora", 98),
    KH2LevelUp("Sora", 99)
]

soraBonusList = [
    KH2Bonus(2,1, locationTypes=["BC"],description="Possessor"),
    KH2Bonus(3,1, locationTypes=["BC"],description="Dark Thorn"),
    KH2Bonus(4,1,locationTypes=["BC"],description="Xaldin"),
    KH2Bonus(5,1,locationTypes=["OC"],description="Cerberus"),
    KH2Bonus(6,1,locationTypes=["OC"],description="Pete (OC)"),
    KH2Bonus(7,1,locationTypes=["OC"],description="Hydra"),
    KH2Bonus(8,1, locationTypes=["OC"],description="Hades"),
    KH2Bonus(9,1,locationTypes=["LoD"],description="Shan-Yu"),
    KH2Bonus(10,1,locationTypes=["LoD"],description="Storm Rider"),
    KH2Bonus(15,1,locationTypes=["HB"],description="Bailey"),
    KH2Bonus(16,1,locationTypes=["DC"],description="Boat Pete"),
    KH2Bonus(17,1,locationTypes=["DC"],description="Wharf Pete"),
    KH2Bonus(18,1,locationTypes=["HT"],description="Prison Keeper"),
    KH2Bonus(21,1,locationTypes=["PR"],description="Barboss"),
    KH2Bonus(22,1,locationTypes=["PR"],description="Grim Reaper 2"),
    KH2Bonus(24,1,locationTypes=["TWTNW"],description="Luxord"),
    KH2Bonus(28,1,locationTypes=["HB"],description="Demyx (Hollow Bastion)"),
    KH2Bonus(30,1,locationTypes=["PL"],description="Groundshaker"),
    KH2Bonus(31,1,locationTypes=["SP"],description="Hostile Program"),
    KH2Bonus(32,1,locationTypes=["SP"],description="MCP"),
    KH2Bonus(33,14,locationTypes=["STT"],description="Twilight Thorn"),
    KH2Bonus(37,1,locationTypes=["Agrabah"],description="Elemental Lords"),
    KH2Bonus(38, 1, locationTypes=["DC"],description="Minnie Escort"),
    KH2Bonus(42,1,locationTypes=["Agrabah"],description="Abu Escort"),
    KH2Bonus(43,1,locationTypes=["LoD"],description="Village Cave"),
    KH2Bonus(47,1,locationTypes=["Agrabah"], invalidChecks=["Fire","Blizzard","Thunder"],description="Genie Jafar"),
    KH2Bonus(54,14,locationTypes=["STT"],description="Station Dusks"),
    KH2Bonus(57,1,locationTypes=["OC"],description="Urns"),
    KH2Bonus(59,1,locationTypes=["PR"],description="Grim Reaper"),
    KH2Bonus(60,1,locationTypes=["HB"],description="1000 Heartless"),
    KH2Bonus(61,1,locationTypes=["SP"],description="Solar Sailer"),
    KH2Bonus(62,1,locationTypes=["PR"],description="Boat Fight"),
    KH2Bonus(63,1,locationTypes=["TT"],description="Betwixt and Between"),
    KH2Bonus(69,1,locationTypes=["TWTNW"],description="Roxas"),
    KH2Bonus(73,14,locationTypes=["STT"],description="Axel 1")
]

formLevels = [
    KH2FormLevel(1,1),
    KH2FormLevel(1,2),
    KH2FormLevel(1,3),
    KH2FormLevel(1,4),
    KH2FormLevel(1,5),
    KH2FormLevel(1,6),
    KH2FormLevel(1,7),
    KH2FormLevel(2,1),
    KH2FormLevel(2,2),
    KH2FormLevel(2,3),
    KH2FormLevel(2,4),
    KH2FormLevel(2,5),
    KH2FormLevel(2,6),
    KH2FormLevel(2,7),
    KH2FormLevel(3,1),
    KH2FormLevel(3,2),
    KH2FormLevel(3,3),
    KH2FormLevel(3,4),
    KH2FormLevel(3,5),
    KH2FormLevel(3,6),
    KH2FormLevel(3,7),
    KH2FormLevel(4,1),
    KH2FormLevel(4,2),
    KH2FormLevel(4,3),
    KH2FormLevel(4,4),
    KH2FormLevel(4,5),
    KH2FormLevel(4,6),
    KH2FormLevel(4,7),
    KH2FormLevel(5,1),
    KH2FormLevel(5,2),
    KH2FormLevel(5,3),
    KH2FormLevel(5,4),
    KH2FormLevel(5,5),
    KH2FormLevel(5,6),
    KH2FormLevel(5,7)
]

keybladeStats = [
    KH2ItemStat(116),
    KH2ItemStat(83),
    KH2ItemStat(84),
    KH2ItemStat(80),
    KH2ItemStat(81),
    KH2ItemStat(82),
    KH2ItemStat(123),
    KH2ItemStat(124),
    KH2ItemStat(127),
    KH2ItemStat(128),
    KH2ItemStat(129),
    KH2ItemStat(130),
    KH2ItemStat(131),
    KH2ItemStat(132),
    KH2ItemStat(133),
    KH2ItemStat(134),
    KH2ItemStat(135),
    KH2ItemStat(136),
    KH2ItemStat(138),
    KH2ItemStat(139),
    KH2ItemStat(137),
    KH2ItemStat(141),
    KH2ItemStat(148),
    KH2ItemStat(140),
    KH2ItemStat(142),
    KH2ItemStat(143),
    KH2ItemStat(149),
    KH2ItemStat(83),
    KH2ItemStat(84),
    KH2ItemStat(85),
    ]