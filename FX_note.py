class FX R&D
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
        Vector field Vel #Project_ParticleFluid
        POP force #Project_Cradence
        
FXnote_Detail
Volume
    Utilization
        Scalar field(density)
            Volumemetric modeling
        Sign distance(SDF)
            Surface modeling
        Vector field
            Force
    Visualizer
        Volume visualization (For density overview)
        Volume Trail (For vel direction)
        vdbvisualizertree
        volumeslice
    Function
        VolumeSample/VolumeSamplev
        Volumepostoindex/Volumeindextopos
        attributeFromVolume
        vdbAnalysis
            Gradient
            CPT
        Volume SOP
        Volume Vop
    Debug
        addpoint/setpoint attribute
