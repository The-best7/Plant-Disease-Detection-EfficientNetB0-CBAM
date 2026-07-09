# c:\Users\Kartik\Downloads\ntcc\plant-disease-app\backend\disease_database.py

DISEASE_DB = {
    "Apple___Apple_scab": {
        "plant_name": "Apple",
        "disease_name": "Apple Scab",
        "status": "Diseased",
        "description": "Apple scab is a severe fungal disease affecting apple trees, causing scabby lesions on leaves, buds, and fruit. It is caused by the ascomycete fungus Venturia inaequalis.",
        "symptoms": [
            "Olive-green, velvety spots on leaf surfaces.",
            "Leaves turn yellow and drop prematurely, causing defoliation.",
            "Brown, corky, cracked spots on the fruit, causing distortion."
        ],
        "causes": [
            "Fungus Venturia inaequalis.",
            "Overwinters in fallen leaves on the orchard floor.",
            "Spring rain and wind release and disperse primary spores (ascospores)."
        ],
        "prevention": [
            "Plant scab-resistant cultivars (e.g., Enterprise, Liberty, GoldRush).",
            "Rake and destroy fallen leaves in autumn to reduce winter spores.",
            "Prune trees to open up the canopy for better air circulation and leaf drying."
        ],
        "organic_remedies": [
            "Apply copper or sulfur-based fungicides early in the spring bud stages.",
            "Spray compost tea to colonize leaves with beneficial microbes.",
            "Apply liquid clay sprays (kaolin) to create a barrier on foliage."
        ],
        "chemical_remedies": [
            "Use protectant fungicides like Captan, Mancozeb, or Chlorothalonil before rain events.",
            "Use systemic fungicides like Myclobutanil (Nova) for post-infection cure.",
            "Rotate fungicide chemical classes (FRAC codes) to avoid resistance."
        ],
        "management_practices": "Water at the soil level rather than overhead. Apply nitrogen to leaf litter in fall to accelerate composting and spore destruction."
    },
    "Apple___Black_rot": {
        "plant_name": "Apple",
        "disease_name": "Black Rot",
        "status": "Diseased",
        "description": "Black rot is a destructive disease of apple trees, causing cankers on limbs, leaf spots (frog-eye leaf spot), and severe fruit rot. It is caused by the fungus Botryosphaeria obtusa.",
        "symptoms": [
            "Frog-eye leaf spots: purple margins with light tan centers.",
            "Black cankers on branches and trunk, causing bark splitting.",
            "Firm, brown-to-black concentric rings of rot on mature fruit, eventually turning it into a shriveled 'mummy'."
        ],
        "causes": [
            "Fungus Botryosphaeria obtusa.",
            "Overwinters in mummified fruit, dead wood, and cankers.",
            "Warm, wet spring weather triggers spore release."
        ],
        "prevention": [
            "Prune out all dead wood, cankers, and fireblight-damaged branches during dormancy.",
            "Remove all mummified fruit from the tree and orchard floor.",
            "Control insect damage to prevent fungal entry points."
        ],
        "organic_remedies": [
            "Spray organic copper-based fungicides from green tip through petal fall.",
            "Use garlic extracts or sulfur sprays during high-risk wet periods.",
            "Apply compost tea to support leaf microbial health."
        ],
        "chemical_remedies": [
            "Apply Captan or Mancozeb sprays at regular intervals from tight cluster to harvest.",
            "Apply Strobilurin fungicides (e.g., Flint, Pristine) for effective control.",
            "Treat pruned cankers with fungicidal sealants."
        ],
        "management_practices": "Burn or bury pruned branches; do not leave them near the orchard. Maintain tree health through optimal watering and fertilization."
    },
    "Apple___Cedar_apple_rust": {
        "plant_name": "Apple",
        "disease_name": "Cedar Apple Rust",
        "status": "Diseased",
        "description": "Cedar apple rust is a common fungal disease requiring two hosts to complete its life cycle: apples/crabapples and Eastern red cedars (junipers). It is caused by Gymnosporangium juniperi-virginianae.",
        "symptoms": [
            "Vibrant yellow-orange circular spots on upper leaf surfaces.",
            "Small cup-like structures (aecia) with tube-like protrusions on lower leaf surfaces.",
            "Orange rust lesions on the calyx end of apple fruit."
        ],
        "causes": [
            "Fungus Gymnosporangium juniperi-virginianae.",
            "Wind-blown spores from galls on nearby red cedars.",
            "Warm spring rain triggers spore discharge from cedar galls."
        ],
        "prevention": [
            "Plant resistant apple varieties (e.g., Honeycrisp, Red Delicious).",
            "Avoid planting Eastern Red Cedars within 2 miles of the apple orchard.",
            "Remove cedar galls from nearby juniper trees in late winter."
        ],
        "organic_remedies": [
            "Apply copper fungicides at the first sign of orange leaf spots.",
            "Apply neem oil or sulfur-based sprays to reduce spore germination.",
            "Prune infected twigs to limit local spread."
        ],
        "chemical_remedies": [
            "Use Myclobutanil (Immunox) or Propiconazole starting at green tip stage.",
            "Use Mancozeb or Chlorothalonil early in the season.",
            "Apply strobilurin fungicides during cedar gall sporulation."
        ],
        "management_practices": "Maintain regular orchard checks. Ensure high sunlight exposure to promote quick drying of apple leaves."
    },
    "Apple___healthy": {
        "plant_name": "Apple",
        "disease_name": "Healthy",
        "status": "Healthy",
        "description": "The apple foliage and fruit show no signs of disease or pest infestation. The leaves are vibrant green and active in photosynthesis.",
        "symptoms": ["No disease symptoms present. Leaf tissue is uniform and green."],
        "causes": ["N/A - Plant is in good health."],
        "prevention": [
            "Maintain regular watering at the base of the plant.",
            "Prune tree annually to maintain open canopy and airflow.",
            "Apply balanced fertilizer according to soil test recommendations."
        ],
        "organic_remedies": [
            "Apply organic compost around the root zone annually.",
            "Spray neem oil occasionally as a preventative measure against insects."
        ],
        "chemical_remedies": [
            "No chemical treatment is required. Avoid pesticide application unless pests are detected."
        ],
        "management_practices": "Monitor regularly for pests and early signs of disease. Keep the base of the tree clear of weeds and debris."
    },
    "Blueberry___healthy": {
        "plant_name": "Blueberry",
        "disease_name": "Healthy",
        "status": "Healthy",
        "description": "The blueberry plant is healthy, showing robust, clean green leaves and no signs of chlorosis, leaf spots, or stem dieback.",
        "symptoms": ["No symptoms of infection or nutritional deficiency. Leaves are healthy and green."],
        "causes": ["N/A - Plant is in good health."],
        "prevention": [
            "Maintain highly acidic soil (pH 4.5 - 5.2) with peat moss or elemental sulfur.",
            "Mulch with pine bark or pine needles to preserve moisture and suppress weeds.",
            "Water deeply, as blueberries have shallow root systems."
        ],
        "organic_remedies": [
            "Apply acidic organic fertilizers (e.g., cottonseed meal, berry fertilizers).",
            "Use pine needle mulch to keep soil organic and acidic."
        ],
        "chemical_remedies": [
            "None required. Maintain soil chemistry to avoid stress-induced diseases."
        ],
        "management_practices": "Prune older canes in late winter to stimulate new, productive growth. Test soil pH annually."
    },
    "Cherry_(including_sour)___Powdery_mildew": {
        "plant_name": "Cherry",
        "disease_name": "Powdery Mildew",
        "status": "Diseased",
        "description": "Powdery mildew of cherry is caused by Podosphaera clandestina. It infects young leaves, shoots, and fruit, leading to stunted growth and reduced crop value.",
        "symptoms": [
            "White, powdery fungal patches on the lower surface of leaves.",
            "Leaves curl upwards, blister, and become distorted.",
            "Infected young shoots become covered in white mycelium and die back."
        ],
        "causes": [
            "Fungus Podosphaera clandestina.",
            "Overwinters in buds and fallen leaf litter.",
            "High humidity and warm temperatures with dry leaves favor disease progression."
        ],
        "prevention": [
            "Prune dense branches to improve air circulation and reduce humidity in the canopy.",
            "Plant trees in sunny areas; shade promotes powdery mildew.",
            "Avoid overhead irrigation which creates high-humidity microclimates."
        ],
        "organic_remedies": [
            "Spray potassium bicarbonate or neem oil on affected leaves.",
            "Use dilute milk sprays (1:9 ratio) under bright sunlight.",
            "Apply sulfur-based sprays before fruit maturation."
        ],
        "chemical_remedies": [
            "Apply Triadimefon or Myclobutanil at first sign of powdery patches.",
            "Use Strobilurins (e.g., Pristine) to control foliage and fruit infection.",
            "Rotate active ingredients to prevent pathogen resistance."
        ],
        "management_practices": "Monitor new vegetative shoots weekly. Keep orchard floor clear of weeds which raise humidity levels."
    },
    "Cherry_(including_sour)___healthy": {
        "plant_name": "Cherry",
        "disease_name": "Healthy",
        "status": "Healthy",
        "description": "The cherry foliage is healthy, showing bright, glossy leaves with no symptoms of fungal leaf spot, rust, or powdery mildew.",
        "symptoms": ["No disease symptoms present. Leaves are green, glossy, and fully expanded."],
        "causes": ["N/A - Plant is in good health."],
        "prevention": [
            "Water trees at the root zone to avoid wetting the foliage.",
            "Apply balanced fertilizer during early spring.",
            "Remove fallen leaves in autumn to prevent disease build-up."
        ],
        "organic_remedies": [
            "Apply a layer of compost each spring to maintain soil organic matter.",
            "Use organic seaweed extract sprays to boost overall plant vigor."
        ],
        "chemical_remedies": [
            "No chemical treatments required. Avoid preventive sprays on healthy trees."
        ],
        "management_practices": "Prune out rubbing or crossing branches in late winter. Paint the lower trunk with white latex paint to prevent winter sunscald."
    },
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "plant_name": "Corn (Maize)",
        "disease_name": "Gray Leaf Spot",
        "status": "Diseased",
        "description": "Gray leaf spot is a devastating fungal disease of corn caused by Cercospora zeae-maydis. It can cause severe leaf necrosis and lodging in susceptible hybrids.",
        "symptoms": [
            "Small, circular tan spots with yellow halos early in the season.",
            "Distinct rectangular, gray-to-brown lesions restricted by leaf veins.",
            "Blighted leaves dry up, leading to premature crop death."
        ],
        "causes": [
            "Fungus Cercospora zeae-maydis.",
            "Overwinters in corn residue left on the soil surface.",
            "Warm temperatures, heavy dew, and prolonged humidity trigger spore production."
        ],
        "prevention": [
            "Plant resistant corn hybrids.",
            "Rotate crops with non-host species (e.g., soybeans, alfalfa) for at least 1-2 years.",
            "Tillage to bury corn residue and accelerate decomposition."
        ],
        "organic_remedies": [
            "Spray neem oil or bio-fungicides based on Bacillus subtilis.",
            "Apply copper soaps early in growth phases to protect leaves.",
            "Ensure proper crop spacing to minimize humidity inside the canopy."
        ],
        "chemical_remedies": [
            "Apply Quinone Outside Inhibitor (QoI) or Demethylation Inhibitor (DMI) fungicides.",
            "Spray fungicides like Azoxystrobin + Propiconazole (Quilt) at tasseling (VT stage).",
            "Treat seeds with systemic fungicides."
        ],
        "management_practices": "Maintain balanced nitrogen fertilization. Avoid overhead pivot irrigation during late afternoons to reduce leaf wetness duration."
    },
    "Corn_(maize)___Common_rust_": {
        "plant_name": "Corn (Maize)",
        "disease_name": "Common Rust",
        "status": "Diseased",
        "description": "Common rust is caused by the fungus Puccinia sorghi. It is characterized by powdery, rust-colored pustules on both leaf surfaces and is highly contagious in cool, moist conditions.",
        "symptoms": [
            "Elongated, golden-brown to cinnamon-brown pustules (uredinia) on upper and lower leaf surfaces.",
            "Pustules rupture, releasing powdery rusty spores.",
            "Leaves turn yellow, dry up, and die in severe cases."
        ],
        "causes": [
            "Fungus Puccinia sorghi.",
            "Spores are carried by wind from southern overwintering regions.",
            "Cool temperatures (16-24°C) and high relative humidity."
        ],
        "prevention": [
            "Plant rust-resistant corn hybrids.",
            "Plant crops early in the season to avoid peak spore migration.",
            "Control weed hosts like Wood Sorrel (Oxalis) which serve as alternate hosts."
        ],
        "organic_remedies": [
            "Apply copper fungicides at the first sign of rust pustules.",
            "Spray compost tea to increase foliar competition against spores.",
            "Dust foliage with fine horticultural sulfur."
        ],
        "chemical_remedies": [
            "Apply Strobilurin or Triazole fungicides (e.g., Pyraclostrobin, Tebuconazole).",
            "Spray immediately if infection levels exceed thresholds on lower leaves prior to tasseling.",
            "Ensure thorough canopy coverage with fungicides."
        ],
        "management_practices": "Ensure proper field drainage. Space crops appropriately for maximum air circulation and sun exposure."
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "plant_name": "Corn (Maize)",
        "disease_name": "Northern Leaf Blight",
        "status": "Diseased",
        "description": "Northern corn leaf blight (NCLB) is caused by Exserohilum turcicum. It creates large cigar-shaped lesions on leaves, reducing photosynthetic capacity and grain fill.",
        "symptoms": [
            "Long, cigar-shaped, grayish-green or tan lesions (1-6 inches long).",
            "Dark, dusty fungal spores inside lesions during humid weather.",
            "Entire leaves wither and die, resembling frost damage."
        ],
        "causes": [
            "Fungus Exserohilum turcicum.",
            "Overwinters in corn residue in soil.",
            "Moderate temperatures (18-27°C) and prolonged dew periods."
        ],
        "prevention": [
            "Select resistant hybrids containing Ht genes.",
            "Perform crop rotation with soybeans, wheat, or oats.",
            "Chop and till corn residue into the soil after harvest."
        ],
        "organic_remedies": [
            "Spray bio-fungicides containing Bacillus amyloliquefaciens.",
            "Use copper sprays as protective barriers.",
            "Spray liquid seaweed extract to boost plant stress tolerance."
        ],
        "chemical_remedies": [
            "Use fungicides like Azoxystrobin (Headline) or Pyraclostrobin.",
            "Fungicide application at early tassel stage offers maximum yield protection.",
            "Rotate fungicide modes of action to prevent resistance."
        ],
        "management_practices": "Maintain balanced fertility (adequate potassium). Avoid continuous corn cropping in fields with a history of NCLB."
    },
    "Corn_(maize)___healthy": {
        "plant_name": "Corn (Maize)",
        "disease_name": "Healthy",
        "status": "Healthy",
        "description": "The corn plant is in excellent health, showing deep green, upright leaves without rust pustules or blight lesions.",
        "symptoms": ["No symptoms of rust, blight, or nutritional chlorosis. Stalk and leaves are strong."],
        "causes": ["N/A - Plant is in good health."],
        "prevention": [
            "Ensure proper crop rotation schemes.",
            "Apply nitrogen, phosphorus, and potassium based on annual soil tests.",
            "Maintain good weed control to prevent host reservoirs."
        ],
        "organic_remedies": [
            "Apply aged compost or organic matter during tillage.",
            "Plant cover crops like rye or clover during the off-season."
        ],
        "chemical_remedies": [
            "No chemical applications required. Practice integrated pest management (IPM)."
        ],
        "management_practices": "Conduct regular crop scouting. Practice zero-tillage selectively only when disease pressures are low."
    },
    "Grape___Black_rot": {
        "plant_name": "Grape",
        "disease_name": "Black Rot",
        "status": "Diseased",
        "description": "Grape black rot is caused by Guignardia bidwellii. It infects all green parts of the vine, turning plump green grapes into dry, hard, shriveled black mummies.",
        "symptoms": [
            "Small, round, cream-colored spots with dark brown borders on leaves.",
            "Small black fruiting bodies (pycnidia) arranged in rings inside leaf spots.",
            "Grapes turn brown, shrivel rapidly, and transform into hard, black mummies."
        ],
        "causes": [
            "Fungus Guignardia bidwellii.",
            "Overwinters in infected canes and shriveled fruit mummies.",
            "Warm, wet weather in spring releases spores that infect new shoots."
        ],
        "prevention": [
            "Prune vines to a trellis system to promote airflow and direct sunlight.",
            "Rake, bury, or destroy all mummified fruit on the ground and vines.",
            "Keep the vineyard floor clean and clear of wild grapevines."
        ],
        "organic_remedies": [
            "Spray copper-based fungicides from bud break until bloom.",
            "Apply sulfur dusts, though they are less effective than copper for black rot.",
            "Remove infected leaves and shoots manually early in the season."
        ],
        "chemical_remedies": [
            "Apply Mancozeb, Captan, or Myclobutanil fungicides starting at bud break.",
            "Strobilurin fungicides (e.g., Abound, Pristine) provide excellent control.",
            "Spray at 7-14 day intervals depending on rainfall frequency."
        ],
        "management_practices": "Ensure canopy management (leaf pulling) to improve spray penetration and reduce humidity around clusters."
    },
    "Grape___Esca_(Black_Measles)": {
        "plant_name": "Grape",
        "disease_name": "Esca (Black Measles)",
        "status": "Diseased",
        "description": "Esca, or Black Measles, is a complex wood disease of grapevines caused by a suite of fungi including Phaeomoniella chlamydospora and Phaeoacremonium minimum, leading to wood rot and leaf stripes.",
        "symptoms": [
            "'Tiger-stripe' leaf patterns: yellow-brown necrotic tissue between green veins.",
            "Tiny, dark purple or black spots ('measles') on grape skin, causing cracking.",
            "Sudden wilting of the entire vine (apoplexy) during hot weather."
        ],
        "causes": [
            "Foliar and wood-colonizing fungi entering through pruning wounds.",
            "Toxins produced by fungi in the grapevine trunk wood.",
            "Older vineyards are more susceptible, but young vines can be affected."
        ],
        "prevention": [
            "Protect pruning wounds immediately with sealants or fungicides.",
            "Prune late in the winter dormant season when spore levels are lower.",
            "Sanitize pruning tools with 70% alcohol or bleach between vines."
        ],
        "organic_remedies": [
            "Apply Trichoderma-based biocontrol agents to pruning wounds.",
            "Apply organic bio-fungicides to trunks to suppress fungal spread.",
            "Prune back infected cordons to healthy white wood."
        ],
        "chemical_remedies": [
            "Paint pruning wounds with Thiophanate-methyl paste.",
            "Use copper compounds on trunks to limit fungal entry.",
            "Systemic chemical treatments are limited; focus is on wound protection."
        ],
        "management_practices": "Mark infected vines during summer and prune them last to prevent spreading the wood rot to healthy vines."
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "plant_name": "Grape",
        "disease_name": "Leaf Blight (Isariopsis)",
        "status": "Diseased",
        "description": "Isariopsis leaf spot is a fungal disease caused by Pseudocercospora vitis. It primarily attacks older grape leaves late in the season, causing premature defoliation.",
        "symptoms": [
            "Dull brown, irregular spots on leaves, starting on lower canopy.",
            "Dark, velvety mold growth on the underside of leaf spots.",
            "Severely affected leaves shrivel, turn brown, and drop off."
        ],
        "causes": [
            "Fungus Pseudocercospora vitis (syn. Isariopsis clavispora).",
            "Overwinters in fallen leaf debris.",
            "Wet conditions and warm temperatures in mid-to-late summer."
        ],
        "prevention": [
            "Ensure regular canopy thinning to keep leaves dry.",
            "Rake and incorporate fallen leaves into the soil to promote rapid decay.",
            "Plant rows in the direction of prevailing winds for quick drying."
        ],
        "organic_remedies": [
            "Spray copper fungicides at the first sign of leaf spots.",
            "Use neem oil or potassium bicarbonate as foliage protectants.",
            "Apply compost tea to support beneficial leaf microflora."
        ],
        "chemical_remedies": [
            "Apply Mancozeb or Chlorothalonil protectant sprays.",
            "Use strobilurin or triazole fungicides if blight spreads early in the season.",
            "Ensure complete coverage of both upper and lower leaf surfaces."
        ],
        "management_practices": "Avoid overhead sprinkler irrigation. Maintain vine vigor through proper soil fertilization."
    },
    "Grape___healthy": {
        "plant_name": "Grape",
        "disease_name": "Healthy",
        "status": "Healthy",
        "description": "The grapevine is in excellent health, showing lush, green leaves, clean shoots, and firm, disease-free grape clusters.",
        "symptoms": ["No disease symptoms present. Leaves are green, thin, and fully functional."],
        "causes": ["N/A - Plant is in good health."],
        "prevention": [
            "Maintain clean canopy pruning annually.",
            "Apply balanced fertilizer during early spring bud break.",
            "Ensure drip irrigation to avoid wetting the leaves."
        ],
        "organic_remedies": [
            "Apply organic compost at the base of the vine.",
            "Plant cover crops like clover between vine rows."
        ],
        "chemical_remedies": [
            "None required. Monitor vines weekly during the growing season."
        ],
        "management_practices": "Train shoots on trellises to manage vine density. Keep the vine trunk base clear of tall grasses."
    },
    "Orange___Haunglongbing_(Citrus_greening)": {
        "plant_name": "Orange",
        "disease_name": "Huanglongbing (Citrus Greening)",
        "status": "Diseased",
        "description": "Citrus greening, or Huanglongbing (HLB), is one of the most destructive citrus diseases in the world. It is caused by Candidatus Liberibacter bacteria, spread by the Asian citrus psyllid, and leads to tree decline.",
        "symptoms": [
            "Asymmetrical, blotchy yellow mottling of leaves (vein yellowing).",
            "Stunted, upright shoots with small, pale leaves.",
            "Small, lopsided, bitter-tasting fruit that remains green at the bottom."
        ],
        "causes": [
            "Bacterium Candidatus Liberibacter asiaticus.",
            "Transmitted by the Asian Citrus Psyllid (Diaphorina citri).",
            "Propagation of infected nursery stock."
        ],
        "prevention": [
            "Use certified disease-free citrus budwood for planting.",
            "Inspect trees frequently for Asian citrus psyllids.",
            "Remove and destroy infected trees immediately to prevent spreading the bacteria."
        ],
        "organic_remedies": [
            "Spray horticultural mineral oils to deter psyllid feeding.",
            "Introduce natural predators like Tamarixia radiata wasps to control psyllids.",
            "Apply nutritional sprays to bolster the tree's immune response."
        ],
        "chemical_remedies": [
            "Apply systemic insecticides (e.g., Imidacloprid) to young trees to control psyllids.",
            "Use foliar sprays of pyrethroids or organophosphates during flush cycles.",
            "Treat infected groves with specific micro-nutrient therapies."
        ],
        "management_practices": "Implement a regional psyllid management program. Maintain strict quarantine regulations on citrus transport."
    },
    "Peach___Bacterial_spot": {
        "plant_name": "Peach",
        "disease_name": "Bacterial Spot",
        "status": "Diseased",
        "description": "Peach bacterial spot is caused by Xanthomonas arboricola pv. pruni. It causes defoliation, twig cankers, and fruit lesions, which reduce tree vigor and fruit marketability.",
        "symptoms": [
            "Water-soaked, angular purple-brown spots on leaves, which dry and drop out leaving a 'shot-hole' appearance.",
            "Severe yellowing of leaves followed by defoliation.",
            "Pitted, dark spots on peach skin, often accompanied by gumming."
        ],
        "causes": [
            "Bacterium Xanthomonas arboricola pv. pruni.",
            "Overwinters in twig cankers and buds.",
            "Warm, wet, windy spring weather spreads the bacteria."
        ],
        "prevention": [
            "Plant resistant peach cultivars (e.g., Loring, Redhaven, Sunhaven).",
            "Maintain high tree vigor with adequate nitrogen fertilization.",
            "Avoid overhead irrigation which spreads bacteria."
        ],
        "organic_remedies": [
            "Apply copper-based sprays during the dormant season and early spring.",
            "Use biopesticides containing Bacillus subtilis.",
            "Spray neem oil to reduce environmental stress."
        ],
        "chemical_remedies": [
            "Spray Oxytetracycline (Mycoshield) at weekly intervals from petal fall to pre-harvest.",
            "Use copper formulations mixed with hydrated lime to prevent leaf burn.",
            "Apply bactericides immediately after severe hailstorms."
        ],
        "management_practices": "Prune trees to allow fast leaf drying. Disinfect pruning tools between trees."
    },
    "Peach___healthy": {
        "plant_name": "Peach",
        "disease_name": "Healthy",
        "status": "Healthy",
        "description": "The peach tree is healthy, displaying rich, dark-green leaves without bacterial spots, rust, or peach leaf curl.",
        "symptoms": ["No disease symptoms present. Leaves are long, green, and intact."],
        "causes": ["N/A - Plant is in good health."],
        "prevention": [
            "Apply a preventive copper spray in late autumn to prevent peach leaf curl.",
            "Maintain regular pruning and clear tree base weeds.",
            "Test soil nutrients and apply organic compost."
        ],
        "organic_remedies": [
            "Apply organic mulch around the tree drip line.",
            "Spray fish emulsion or seaweed fertilizer on roots."
        ],
        "chemical_remedies": [
            "No chemical treatments required. Avoid unnecessary spraying."
        ],
        "management_practices": "Thin peaches early in summer to prevent limb breakage and improve fruit size."
    },
    "Pepper,_bell___Bacterial_spot": {
        "plant_name": "Pepper, Bell",
        "disease_name": "Bacterial Spot",
        "status": "Diseased",
        "description": "Bacterial spot of bell pepper is caused by Xanthomonas campestris pv. vesicatoria. It can cause rapid defoliation and severe fruit spotting in warm, humid climates.",
        "symptoms": [
            "Small, circular, raised dark spots on lower leaf surfaces.",
            "Spots turn brown, enlarge, and coalesce, causing leaves to yellow and drop.",
            "Raised, blister-like rough lesions on the pepper fruit."
        ],
        "causes": [
            "Bacterium Xanthomonas campestris pv. vesicatoria.",
            "Infected seed or infected plant debris in the soil.",
            "Rain splash and overhead irrigation spread bacteria."
        ],
        "prevention": [
            "Buy certified disease-free seeds and transplants.",
            "Rotate pepper crops with non-solanaceous crops for 2-3 years.",
            "Avoid working in pepper fields when foliage is wet."
        ],
        "organic_remedies": [
            "Spray copper-based organic bactericides every 7-10 days.",
            "Use Bacillus subtilis bio-bactericides.",
            "Mulch plants with straw or plastic to prevent soil splash."
        ],
        "chemical_remedies": [
            "Apply copper-mancozeb tank mixes for enhanced control.",
            "Spray streptomycin in seedling stages if bacterial spot is detected.",
            "Ensure comprehensive foliage coverage."
        ],
        "management_practices": "Drip irrigate peppers. Pull and destroy infected plants immediately upon detection."
    },
    "Pepper,_bell___healthy": {
        "plant_name": "Pepper, Bell",
        "disease_name": "Healthy",
        "status": "Healthy",
        "description": "The bell pepper foliage is clean and healthy, with uniform dark green leaves and no spots, wilting, or yellowing.",
        "symptoms": ["No signs of disease or nutritional stress. Foliage is clean and green."],
        "causes": ["N/A - Plant is in good health."],
        "prevention": [
            "Drip irrigate pepper plants.",
            "Provide support cages to keep foliage off the ground.",
            "Apply organic nitrogen fertilizer during early bloom."
        ],
        "organic_remedies": [
            "Apply organic compost at planting.",
            "Spray neem oil to prevent aphid infestations."
        ],
        "chemical_remedies": [
            "No chemical treatments required. Practice preventive monitoring."
        ],
        "management_practices": "Maintain consistent soil moisture to prevent blossom-end rot in peppers."
    },
    "Potato___Early_blight": {
        "plant_name": "Potato",
        "disease_name": "Early Blight",
        "status": "Diseased",
        "description": "Early blight is a common disease of potato crops caused by Alternaria solani. It targets older foliage first, causing brown spots with concentric ring patterns.",
        "symptoms": [
            "Dark brown to black spots with concentric rings ('target board' appearance) on older leaves.",
            "Yellow halo surrounding the leaf spots.",
            "Dry, brown, leathery sunken lesions on potato tubers."
        ],
        "causes": [
            "Fungus Alternaria solani.",
            "Overwinters in infected potato crop residue.",
            "Alternating wet and dry conditions favor spore development and dispersal."
        ],
        "prevention": [
            "Plant certified disease-free seed tubers.",
            "Choose early-maturing cultivars or varieties with partial resistance.",
            "Rotate potatoes with grains or legumes."
        ],
        "organic_remedies": [
            "Spray copper fungicides at first sign of target spots.",
            "Use bio-fungicides based on Bacillus subtilis.",
            "Apply mulch to prevent soil-borne spores from splashing onto lower leaves."
        ],
        "chemical_remedies": [
            "Apply Chlorothalonil, Mancozeb, or Azoxystrobin.",
            "Spray weekly when weather conditions are warm and humid.",
            "Rotate chemical classes to prevent resistance."
        ],
        "management_practices": "Water potatoes at the base using drip irrigation. Destroy or harvest potato foliage (vine killing) two weeks before tuber harvest to toughen skins."
    },
    "Potato___Late_blight": {
        "plant_name": "Potato",
        "disease_name": "Late Blight",
        "status": "Diseased",
        "description": "Late blight is a devastating disease of potatoes and tomatoes caused by the oomycete Phytophthora infestans. It was the pathogen responsible for the Irish Potato Famine and can destroy entire fields in days.",
        "symptoms": [
            "Large, dark, water-soaked leaf spots turning black, often starting at leaf tips.",
            "White, velvety mold growth on leaf undersides in humid weather.",
            "Tubers display a copper-brown, dry, corky rot."
        ],
        "causes": [
            "Oomycete Phytophthora infestans.",
            "Spores blown in by wind from infected fields or cull piles.",
            "Cool, wet, cloudy, and highly humid weather conditions."
        ],
        "prevention": [
            "Plant resistant potato cultivars (e.g., Defender, Jacqueline Lee).",
            "Eliminate all cull piles (dumped waste potatoes) near fields.",
            "Drip irrigate; avoid overhead watering."
        ],
        "organic_remedies": [
            "Apply copper fungicides preventatively during cool, wet periods.",
            "Use copper octanoate or copper soap sprays.",
            "Apply bio-fungicides containing Bacillus amyloliquefaciens."
        ],
        "chemical_remedies": [
            "Apply systemic oomycete-specific fungicides like Mefenoxam or Fluopicolide.",
            "Apply protectants like Mancozeb or Chlorothalonil early in the season.",
            "Spray at high pressure to ensure deep canopy penetration."
        ],
        "management_practices": "Harvest potatoes only after vines have been dead for 10-14 days. Store tubers in dry, well-ventilated locations."
    },
    "Potato___healthy": {
        "plant_name": "Potato",
        "disease_name": "Healthy",
        "status": "Healthy",
        "description": "The potato plant is healthy, showing bright green compound leaves with no blight lesions or target-board spots.",
        "symptoms": ["No disease symptoms present. Vigorous green vine growth."],
        "causes": ["N/A - Plant is in good health."],
        "prevention": [
            "Plant certified seed potatoes.",
            "Hill potatoes regularly to protect tubers from sunlight and blight spores.",
            "Keep potato rows clean and weed-free."
        ],
        "organic_remedies": [
            "Incorporate green manure or compost during soil prep.",
            "Apply organic nitrogen fertilizer to support vine growth."
        ],
        "chemical_remedies": [
            "No chemical treatments required. Routine field scouting."
        ],
        "management_practices": "Ensure deep hilling of potato plants to keep developing tubers covered in soil."
    },
    "Raspberry___healthy": {
        "plant_name": "Raspberry",
        "disease_name": "Healthy",
        "status": "Healthy",
        "description": "The raspberry plant is healthy, showing clean green compound leaves with no rust spots, powdery mildew, or cane cankers.",
        "symptoms": ["No symptoms of infection. Canes and leaves are strong and green."],
        "causes": ["N/A - Plant is in good health."],
        "prevention": [
            "Prune floricanes (second-year fruiting canes) to the ground immediately after harvest.",
            "Trellis canes to maximize airflow and sunlight entry.",
            "Maintain a weed-free zone around raspberry rows."
        ],
        "organic_remedies": [
            "Mulch canes with organic compost or straw.",
            "Spray compost tea to protect canes from aerial spores."
        ],
        "chemical_remedies": [
            "None required. Maintain cultural practices to prevent cane blight."
        ],
        "management_practices": "Drip irrigate raspberries. Avoid excessive nitrogen fertilizer which causes soft canes."
    },
    "Soybean___healthy": {
        "plant_name": "Soybean",
        "disease_name": "Healthy",
        "status": "Healthy",
        "description": "The soybean crop is healthy, showing uniform green trifoliate leaves, strong stems, and no rust, leaf spots, or mildew.",
        "symptoms": ["No disease symptoms present. Leaves are green, clean, and robust."],
        "causes": ["N/A - Plant is in good health."],
        "prevention": [
            "Use certified disease-free soybean seeds.",
            "Rotate soybean crops with corn, wheat, or oats.",
            "Maintain optimal crop planting density."
        ],
        "organic_remedies": [
            "Incorporate compost into soil prior to planting.",
            "Inoculate seeds with beneficial nitrogen-fixing Bradyrhizobium bacteria."
        ],
        "chemical_remedies": [
            "No chemical treatments required. Practice regular crop scouting."
        ],
        "management_practices": "Scout fields regularly for insect pests like soybean aphids, which can vector viruses."
    },
    "Squash___Powdery_mildew": {
        "plant_name": "Squash",
        "disease_name": "Powdery Mildew",
        "status": "Diseased",
        "description": "Powdery mildew of squash is caused by Podosphaera xanthii. It covers leaves in a white powdery talc, reducing photosynthesis and causing leaves to wither and die.",
        "symptoms": [
            "White, talcum-powder-like spots on upper and lower surfaces of leaves and stems.",
            "Leaves turn yellow, dry up, brown, and become brittle.",
            "Sunburn on squash fruit due to defoliation."
        ],
        "causes": [
            "Fungus Podosphaera xanthii.",
            "Spreads by wind-borne spores.",
            "High humidity, moderate temperatures (20-27°C), and shaded areas."
        ],
        "prevention": [
            "Plant resistant squash cultivars.",
            "Ensure full sun exposure for squash beds.",
            "Provide ample spacing between squash plants to ensure airflow."
        ],
        "organic_remedies": [
            "Spray neem oil, jojoba oil, or horticultural oils on leaves.",
            "Apply potassium bicarbonate or baking soda sprays (1 tbsp baking soda + 1 tsp liquid soap in 1 gallon water).",
            "Spray dilute milk solutions weekly."
        ],
        "chemical_remedies": [
            "Apply Myclobutanil or Triadimefon fungicides.",
            "Apply Chlorothalonil early in the season as a protectant.",
            "Rotate chemical classes to prevent fungal resistance."
        ],
        "management_practices": "Avoid overhead watering. Prune older, heavily infected lower leaves to reduce spore load."
    },
    "Strawberry___Leaf_scorch": {
        "plant_name": "Strawberry",
        "disease_name": "Leaf Scorch",
        "status": "Diseased",
        "description": "Strawberry leaf scorch is caused by Diplocarpon earlianum. It infects leaves, petioles, runners, and fruit pedicels, mimicking drought stress by turning leaves brown and dry.",
        "symptoms": [
            "Small, dark-purple spots on upper leaf surfaces.",
            "Spots enlarge and merge, turning the leaf tissue brown, curled, and dried ('scorched').",
            "Purple streaks on runners and leaf stems."
        ],
        "causes": [
            "Fungus Diplocarpon earlianum.",
            "Overwinters in infected leaf debris.",
            "Warm temperatures and long periods of leaf wetness."
        ],
        "prevention": [
            "Plant resistant strawberry varieties (e.g., Allstar, Tribute).",
            "Plant strawberries in raised beds to ensure good drainage.",
            "Mow leaves in renovated beds after harvest to destroy old foliage."
        ],
        "organic_remedies": [
            "Spray copper-based organic fungicides early in the spring.",
            "Use sulfur-based sprays before bloom.",
            "Remove infected leaves manually and burn them."
        ],
        "chemical_remedies": [
            "Apply Captan or Thiram protectant fungicides.",
            "Apply systemic fungicides like Thiophanate-methyl if infection is severe.",
            "Ensure thorough coverage of both leaf surfaces."
        ],
        "management_practices": "Ensure strawberries are weeded to improve wind airflow. Drip irrigate."
    },
    "Strawberry___healthy": {
        "plant_name": "Strawberry",
        "disease_name": "Healthy",
        "status": "Healthy",
        "description": "The strawberry plant is healthy, showing bright green leaves, clean runners, and bright white flowers.",
        "symptoms": ["No disease symptoms present. Leaves are green, serrated, and healthy."],
        "causes": ["N/A - Plant is in good health."],
        "prevention": [
            "Mulch beds with clean straw to keep berries off the soil.",
            "Drip irrigate at base of plant.",
            "Fertilize with organic fish emulsion in early spring."
        ],
        "organic_remedies": [
            "Apply organic compost at planting.",
            "Use straw mulch to preserve clean foliage."
        ],
        "chemical_remedies": [
            "No chemical treatments required. Practice preventive scouting."
        ],
        "management_practices": "Renovate strawberry beds annually after harvest. Replace strawberry plants every 3 years."
    },
    "Tomato___Bacterial_spot": {
        "plant_name": "Tomato",
        "disease_name": "Bacterial Spot",
        "status": "Diseased",
        "description": "Tomato bacterial spot is caused by Xanthomonas species (X. vesicatoria, X. perforans, X. gardneri, X. euvesicatoria). It causes leaf lesions, defoliation, and fruit scabs.",
        "symptoms": [
            "Small, dark, water-soaked spots with yellow-green halos on leaves.",
            "Leaf spots turn brown and dry out, eventually causing leaves to drop.",
            "Small, raised, scab-like spots with dark margins on the green and red tomato fruit."
        ],
        "causes": [
            "Bacteria Xanthomonas spp.",
            "Infected seed or infected soil-borne debris.",
            "Warm, wet, windy weather that spreads bacteria via rain splash."
        ],
        "prevention": [
            "Use certified disease-free seed and transplants.",
            "Rotate tomato crop with non-solanaceous crops for 2-3 years.",
            "Avoid overhead irrigation; use drip tapes instead."
        ],
        "organic_remedies": [
            "Apply copper-based fungicides/bactericides every 7 days during warm, wet weather.",
            "Spray Bacillus subtilis bio-bactericides to protect leaves.",
            "Mulch plants with straw to prevent soil splash."
        ],
        "chemical_remedies": [
            "Apply copper-mancozeb tank mixes for maximum bactericidal efficacy.",
            "Use Actigard (acibenzolar-S-methyl) to trigger systemic acquired resistance.",
            "Apply bactericides early in the day so foliage dries quickly."
        ],
        "management_practices": "Prune lower tomato leaves to prevent contact with soil. Destroy infected plant residues at the end of the season."
    },
    "Tomato___Early_blight": {
        "plant_name": "Tomato",
        "disease_name": "Early Blight",
        "status": "Diseased",
        "description": "Tomato early blight is a common fungal disease caused by Alternaria solani. It targets lower leaves first, producing brown target-board lesions, and can cause significant yield loss.",
        "symptoms": [
            "Dark spots with concentric rings (target-like) on older, lower leaves.",
            "Yellowing leaf borders surrounding the brown spots.",
            "Sunken, leathery black lesions on the stem end of tomato fruit."
        ],
        "causes": [
            "Fungus Alternaria solani.",
            "Fungal spores overwinter in soil and tomato crop residue.",
            "Warm, wet weather combined with plant stress (e.g., heavy fruit load)."
        ],
        "prevention": [
            "Plant resistant tomato cultivars (e.g., Defiant, Iron Lady).",
            "Prune the lower 12-18 inches of tomato branches to prevent soil contact.",
            "Rotate crops; do not plant tomatoes, potatoes, or peppers in the same spot for 3 years."
        ],
        "organic_remedies": [
            "Apply organic copper-based or sulfur-based fungicides immediately after spotting begins.",
            "Spray neem oil or bio-fungicides containing Bacillus amyloliquefaciens.",
            "Mulch the soil surface around plants to act as a spore barrier."
        ],
        "chemical_remedies": [
            "Spray Chlorothalonil or Mancozeb protectants.",
            "Use systemic fungicides like Difenoconazole or Azoxystrobin for active infections.",
            "Keep spraying at 7-14 day intervals during wet periods."
        ],
        "management_practices": "Stake and cage tomatoes to keep foliage off the ground. Avoid overhead sprinklers."
    },
    "Tomato___Late_blight": {
        "plant_name": "Tomato",
        "disease_name": "Late Blight",
        "status": "Diseased",
        "description": "Late blight is a fast-moving, highly destructive oomycete disease caused by Phytophthora infestans. It can destroy healthy tomato fields in days during cool, wet weather.",
        "symptoms": [
            "Large, irregular, water-soaked dark green to black lesions on leaves and stems.",
            "White, downy fungal-like growth on the undersides of leaves during wet weather.",
            "Large, firm, greasy golden-brown patches on green and red fruit."
        ],
        "causes": [
            "Oomycete Phytophthora infestans.",
            "Wind-blown spores from infected potato or tomato plants.",
            "Cool (15-22°C), wet, cloudy, and humid conditions."
        ],
        "prevention": [
            "Plant late blight resistant varieties (e.g., Mountain Magic, Plum Regal).",
            "Eliminate potato cull piles and volunteer tomato plants.",
            "Space plants widely to ensure fast leaf drying."
        ],
        "organic_remedies": [
            "Apply copper fungicides (copper hydroxide or copper octanoate) preventatively.",
            "Use bio-fungicides containing Bacillus amyloliquefaciens.",
            "Destroy infected plants immediately: pull, bag, and discard (do not compost)."
        ],
        "chemical_remedies": [
            "Apply systemic oomycete-specific fungicides like Mandipropamid (Revus) or Mefenoxam.",
            "Spray Chlorothalonil or Mancozeb as a preventive shield.",
            "Monitor local agricultural alerts for late blight spores in your area."
        ],
        "management_practices": "Avoid overhead watering. Maintain crop rotations and clean up all host debris in autumn."
    },
    "Tomato___Leaf_Mold": {
        "plant_name": "Tomato",
        "disease_name": "Leaf Mold",
        "status": "Diseased",
        "description": "Tomato leaf mold is caused by Passalora fulva (syn. Fulvia fulva). It is a major fungal disease in greenhouse tomatoes where humidity is high and air movement is restricted.",
        "symptoms": [
            "Pale green or yellow spots on the upper leaf surfaces.",
            "Olive-green to purple-brown velvety mold growth on the lower surface of the leaf spots.",
            "Leaves curl, wither, and drop, resulting in defoliation."
        ],
        "causes": [
            "Fungus Passalora fulva.",
            "Overwinters in crop debris and greenhouse structures.",
            "Relative humidity above 85% and warm temperatures (21-24°C)."
        ],
        "prevention": [
            "Use resistant tomato cultivars.",
            "Provide excellent greenhouse ventilation: use fans and horizontal air flow systems.",
            "Heat greenhouses at night to reduce relative humidity."
        ],
        "organic_remedies": [
            "Apply copper-based fungicides to the underside of leaves.",
            "Use bio-fungicides based on Bacillus subtilis.",
            "Manually remove and discard infected leaves."
        ],
        "chemical_remedies": [
            "Apply Chlorothalonil or Mancozeb preventatively.",
            "Use systemic fungicides like Azoxystrobin or Pyraclostrobin.",
            "Ensure complete coverage of both upper and lower leaf surfaces."
        ],
        "management_practices": "Drip irrigate tomatoes. Space rows widely to allow workers to prune leaves easily."
    },
    "Tomato___Septoria_leaf_spot": {
        "plant_name": "Tomato",
        "disease_name": "Septoria Leaf Spot",
        "status": "Diseased",
        "description": "Septoria leaf spot is caused by the fungus Septoria lycopersici. It causes numerous small, circular spots on lower leaves, leading to severe defoliation and sunscalded fruit.",
        "symptoms": [
            "Numerous small, circular spots (1/16 to 1/8 inch) with dark borders and tan-to-white centers on lower leaves.",
            "Tiny black specks (pycnidia) inside the centers of the leaf spots.",
            "Leaves turn yellow, dry up, and drop, starting from the base of the plant."
        ],
        "causes": [
            "Fungus Septoria lycopersici.",
            "Spore survival on solanaceous weeds (like horse nettle) and crop debris.",
            "Rain splash and leaf wetness favor infection."
        ],
        "prevention": [
            "Maintain a 3-year crop rotation without solanaceous crops.",
            "Keep fields clear of solanaceous weeds.",
            "Mulch soil heavily with straw or plastic."
        ],
        "organic_remedies": [
            "Apply organic copper hydroxide sprays at the first sign of lower leaf spots.",
            "Use Bacillus-based bio-fungicides.",
            "Prune infected lower leaves and wash hands before touching other plants."
        ],
        "chemical_remedies": [
            "Apply Chlorothalonil or Mancozeb regularly.",
            "Use Strobilurins (e.g., Cabrio) for high-efficiency control.",
            "Repeat sprays every 7-10 days in rainy seasons."
        ],
        "management_practices": "Drip irrigate. Stake and prune tomatoes to keep foliage high above the soil."
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "plant_name": "Tomato",
        "disease_name": "Two-Spotted Spider Mite",
        "status": "Diseased",
        "description": "Two-spotted spider mites (Tetranychus urticae) are microscopic arachnid pests. They suck cell contents from tomato leaves, causing stippling, webbing, and rapid leaf drop in dry, hot weather.",
        "symptoms": [
            "Tiny yellow or white specks (stippling) on the upper surface of leaves.",
            "Fine, silk-like webbing on the undersides of leaves and stems.",
            "Leaves turn bronze or yellow, dry up, and drop off."
        ],
        "causes": [
            "Mite pest Tetranychus urticae.",
            "Hot, dry, dusty weather conditions.",
            "Overuse of broad-spectrum chemical insecticides which kill natural predators."
        ],
        "prevention": [
            "Release predatory mites (e.g., Phytoseiulus persimilis) as biocontrol agents.",
            "Keep plants well-watered; drought-stressed plants attract mites.",
            "Hose down dusty farm roads to prevent mites from traveling on dust."
        ],
        "organic_remedies": [
            "Spray with insecticidal soaps or horticultural oils (e.g., neem oil).",
            "Blast the undersides of leaves with strong streams of water to break webs and wash away mites.",
            "Apply rosemary oil-based organic miticides."
        ],
        "chemical_remedies": [
            "Apply specific miticides/acaricides like Abamectin, Spiromesifen, or Bifenazate.",
            "Avoid pyrethroid insecticides, which can cause mite flare-ups.",
            "Ensure spray reaches the underside of the foliage."
        ],
        "management_practices": "Scout the lower leaf surfaces using a 10x hand lens. Keep greenhouse humidity moderate."
    },
    "Tomato___Target_Spot": {
        "plant_name": "Tomato",
        "disease_name": "Target Spot",
        "status": "Diseased",
        "description": "Target spot is caused by the fungus Corynespora cassiicola. It affects leaves, stems, and fruit, resembling early blight with circular lesions but different spore structures.",
        "symptoms": [
            "Circular, brown spots (1/8 to 3/8 inch) with light brown centers and faint concentric rings.",
            "Lesions on the tomato fruit start as small, slightly sunken brown flecks.",
            "Petioles and stems show elongated dark brown spots."
        ],
        "causes": [
            "Fungus Corynespora cassiicola.",
            "Overwinters in infected crop debris.",
            "High humidity and temperatures around 20-28°C."
        ],
        "prevention": [
            "Select resistant cultivars.",
            "Maintain crop rotation with corn or grass crops.",
            "Prune tomato suckers and lower foliage to promote canopy ventilation."
        ],
        "organic_remedies": [
            "Apply copper-based fungicides at the first sign of disease.",
            "Use organic bio-fungicides based on Bacillus strains.",
            "Mulch rows with straw to prevent ground spores from splashing."
        ],
        "chemical_remedies": [
            "Apply Chlorothalonil or Mancozeb sprays.",
            "Use systemic fungicides like Azoxystrobin or Boscalid.",
            "Rotate chemical groups to avoid resistance development."
        ],
        "management_practices": "Avoid working in fields when leaves are wet. Keep fields clear of weed hosts."
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "plant_name": "Tomato",
        "disease_name": "Tomato Yellow Leaf Curl Virus",
        "status": "Diseased",
        "description": "Tomato Yellow Leaf Curl Virus (TYLCV) is a destructive viral disease transmitted by the silverleaf whitefly. It causes extreme leaf curling, chlorosis, and stunting, often leading to zero fruit yield if infection occurs early.",
        "symptoms": [
            "Severe upward curling and cupping of young leaves.",
            "Leaf margins turn bright yellow (chlorosis).",
            "Severe stunting of the plant with a bunchy, bushy appearance and failure to set fruit."
        ],
        "causes": [
            "Tomato Yellow Leaf Curl Virus (Begomovirus).",
            "Vectored by the silverleaf whitefly (Bemisia tabaci).",
            "Infected volunteer tomato plants or weed hosts."
        ],
        "prevention": [
            "Plant TYLCV-resistant tomato cultivars.",
            "Use UV-reflective silver plastic mulches to repel whiteflies.",
            "Install insect-proof screens (50-mesh) on greenhouse vents."
        ],
        "organic_remedies": [
            "Spray insecticidal soaps, neem oil, or horticultural oils to suppress whitefly nymphs.",
            "Release beneficial insects like Lacewings or Encarsia formosa wasps.",
            "Use yellow sticky cards to trap adult whiteflies."
        ],
        "chemical_remedies": [
            "Apply systemic insecticides (e.g., Imidacloprid, Dinotefuran) at transplanting.",
            "Spray foliar insecticides (e.g., Cyantraniliprole, Spirotetramat) for whitefly control.",
            "Rotate insecticide chemistry groups to avoid whitefly resistance."
        ],
        "management_practices": "Pull, double-bag, and destroy infected plants immediately. Clean crop residues immediately after final harvest."
    },
    "Tomato___Tomato_mosaic_virus": {
        "plant_name": "Tomato",
        "disease_name": "Tomato Mosaic Virus",
        "status": "Diseased",
        "description": "Tomato mosaic virus (ToMV) is a highly stable, easily transmitted viral pathogen. It causes mottled green patterns on leaves, stunted growth, and internal browning of fruit.",
        "symptoms": [
            "Mottled green and yellow mosaic patterns on leaves.",
            "Leaves become thin and narrow, resembling a shoestring ('fern-leaf' symptom).",
            "Fruit exhibits internal brown necrotic walls and matures unevenly."
        ],
        "causes": [
            "Tomato Mosaic Virus (Tobamovirus).",
            "Mechanical transmission via hands, tools, or clothing.",
            "Infected seed or survival in crop residue in soil."
        ],
        "prevention": [
            "Plant ToMV-resistant cultivars.",
            "Soak seeds in a 10% trisodium phosphate (TSP) solution to remove surface virus.",
            "Sanitize hands and tools in skim milk or disinfectant before working with tomatoes."
        ],
        "organic_remedies": [
            "There are no organic remedies once infected; immediately pull and burn plants.",
            "Spray milk solutions (virus particles bind to proteins, reducing spread).",
            "Use fresh soil for seedlings."
        ],
        "chemical_remedies": [
            "Viruses cannot be cured chemically. Prevent mechanical spread.",
            "Sanitize greenhouse benches and stakes with virucidal solutions."
        ],
        "management_practices": "Avoid smoking or handling tobacco (which can carry TMV/ToMV) before working in tomatoes. Prune and work in healthy blocks first, then infected ones."
    },
    "Tomato___healthy": {
        "plant_name": "Tomato",
        "disease_name": "Healthy",
        "status": "Healthy",
        "description": "The tomato plant is healthy, showing bright green compound leaves, a sturdy stem, and clean flower clusters.",
        "symptoms": ["No disease symptoms present. Vigorous vegetative growth."],
        "causes": ["N/A - Plant is in good health."],
        "prevention": [
            "Drip irrigate at the base of the plant.",
            "Stake plants and prune lower suckers to maintain canopy airflow.",
            "Apply balanced fertilizer during early planting and fruit set."
        ],
        "organic_remedies": [
            "Apply organic compost at planting.",
            "Mulch roots with straw to preserve moisture."
        ],
        "chemical_remedies": [
            "No chemical treatments required. Practice regular monitoring."
        ],
        "management_practices": "Maintain regular weeding and prune lower leaves to prevent splash infection."
    }
}

PLANT_CLASSES = list(DISEASE_DB.keys())
