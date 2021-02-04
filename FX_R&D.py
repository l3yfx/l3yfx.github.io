class FX_Res
    def VDB
        Theory
            Efficient memory and fast data access.
            No topology restrictions.
        Context
            *Manipulate voxel data to create 3D mesh(fog,smoke,fire,fluid,fracture,abstractGeo)
                # vdbAnalysis(gradient,cpt,.....)                  
            *Store data in voxel to tansfer data.
                # attributeFromVolume
        Utilization
            Scalar field(density)
                Volumemetric modeling
            Signed distance field(SDF)
                Surface modeling
            Vector field
                Vel, Force
        Function
            VolumeSample/VolumeSamplev
            Volumepostoindex/Volumeindextopos
            attributeFromVolume
            vdbAnalysis
                Gradient
                CPT
            Volume Vop                
        Visualizer
            Volume visualization (For density overview)
            Volume Trail (For vel direction)
            vdbvisualizertree
            volumeslice
        Debug
            addpoint/setpoint attribute        
class FX_Dev
	def Growth
    # 1 way transform.
        Copy&Instance #Project_Crassula
        Noise + @P transform #Project_SnakeIsland
        Move & trail #Project_NikeFlyknit
        VDB modeling #Project_Organic
    def Morph
    # 2 ways transform.          
        UV xform #Project_LineMorph #Project_Venus
        @P mix function #Project_Knitting
    def Magic
        Vector field Vel & SDF #Project_ParticleFluid
        POP force #Project_Cradence
        