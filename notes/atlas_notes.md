# Notes about Atlases

**Look into Allen Brain Atlas and ICBM15**

[History](https://www.ncbi.nlm.nih.gov/pubmed/22248580)

- ^This one is relevant towards fMRI
- Used to be based on single patients, but became more sophisticated after MRIs
- Coordinate-based (Spatial location)
    - Talairach et. al was one of the first atlases (1967), 3D coordinate space for brain surgeries
        - Relies on glabella-inion line (AC-PC line), which goes from top of AC to bottom of PC
        - Generated from single 60yo female brain
        - Asymmetry ignored (which causes problems during cortical analysis)
        - Current researchers use piecewise scaling to match the atlas, which can lead to localization errors
    - Alternative was MNI space (MNI305)
        - 305 subjects used, landmarks on each brain identified using Talairach space and then registered using least-squares linear regression
        - Colin27 was higher defintion MNI305
            - Based on single subject scanned 27 times and images registered to MNI305
            - Doesn't really capture anatomy and more for segmentation
        - MN152 = ~150 subjects from 3 locations scanned and registered to MNI305 for high definition
        - ICBM 452 has 452 subjects and adds nonlinear registration to match to MNI305
- Volume-based (Volumetric Parcellation) w/ probabilities that each part belongs to region
    - MNI and Talairach also converted to volume-based versions
    - Harvard-Oxford from 37 subjects, 48 overall regions w/ 21 subcortical regions
    - Freesurfer (40 subjects), 74 cortical labels/hemisphere
    - LPBA40 (10 subjects), manually labeled
    - AAL = Colin27 nonlinearly warped to MNI152 space and then segmented into 45 parts/hemisphere
    - Cytoarchitecture based on microscopy
- Domain-specific exist (for specific diseases/aging/pediatrics, etc.)
- For fMRI, cortical folding patterns matter
- Mapping between spaces and volumes can cause significant differences in locations (+2 to 3.5 mm)

[Comparing](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2748707/)
- No widely accepted standard exists, each person thinks they can add a better one
- This article compares strictly anatomical definitions for regions
- Overall, for some atlases, it makes no difference to use one or the other
- (Check https://www.nitrc.org/projects/obart/ later)
- Different atlases obviously have different parcellations
- Not just a terminology issue, has far reaching effects
- This article also agrees that Talairach was established early, leading to its wide usage even though it has problems
- To compare brain atlases, need to register them to the same brain/common template
- Easier way to phrase: "What is the probability that a voxel is in Region X according to Method A if it is in Region Y according to Method B?" [Venn Diagram](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2748707/figure/pone-0007200-g002/)
- This article includes AAL, CYTO, ICBM, LPBA40, TALc atlases
- Compared to random parcellations as well
- All were dissimilar from random, except TALc, which had registration difficulties

[fMRI atlas generation](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3838923/)
- Need to represent "functional connectivity patterns"
- Compared against Talairach and Tournoux, Harvard-Oxford, Eickoff-Zilles, and Automatic Anatomical Labeling as well as just random parcellation
- Require
    - functional homogeneity (connected regions)
    - spatial contiguous
    - Group-level parcellation should fit individuals
    - Individual voxels should fit into parcellation
- Could try to define ROI based on research, but it's all just hypothesizing and not really based on data
- Could also use previous atlases, but don't really separate based on function
- Anatomical atlases are also higher resolution than fMRI images so could cause errors when applied
- Anatomical ROI's and functional ROI's don't necessarily match
- Use normalized cut method (NCUT) to cluster resting state data
- Convert each voxel to a node and turn whole brain into a graph, edge weights correspond to similarity between nodes
    - Edges removed iteratively until specified number of clusters reached based on similarity between clusters
    - Basically spectral clustering
- Do you choose temporal or spatial similarity more? How many clusters?

- Each edge cut has a cost and to implement this method, all they did was just normalize the cost by the total edge weights in the specified regions (cut(A,B) * (1/assoc(A, V) + 1/assoc(B, V)))
- Group level done by averaging individual graphs together
- Used Dice Coefficient to measure similarity between graphs
- Used New York University test-retest [data set](http://fcon_1000.projects.nitrc.org/)
- 
