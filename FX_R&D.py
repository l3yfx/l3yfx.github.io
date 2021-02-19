class FX_Res
    def SOP
        Geometry component
            Point,vertex,primitive,detail  
                Attributes
                    Context
                        Point,vertex,primitive,detail                                            
                    Reserved/Custom attributes
                        P,Normal,UVs,V,pscale
                Primitive
                    Bezier/NURBS
                    Volume
                        Scalar field(density)
                        Sign distance(SDF)
                        Vector field
                    PointCloud
    def VDB
        Theory
            Efficient memory and fast data access.
            No topology restrictions.
        Context
            *Manipulate voxel data to create 3D mesh(fog,smoke,fire,fluid,fracture,meshing)
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
            vdbactivate
            vdbAdvect
            vdbSmooth
            SDF collider        
        Visualizer
            Volume visualization (For density overview)
            Volume Trail (For vel direction)
            vdbvisualizertree
            volumeslice
        Debug
            addpoint/setpoint attribute
        Rendering
            Mantra rendering Isosurface(SDF volume)
        # VDB_Meshing
    		VDB vs Houdini standard volume
    			VDBFrom polygon
    				Exterior/Interior band -> Data caculation efficiency, "Sparse data structure".
    				Surface attribute -> transfer attribute to volume data
    			VDBSmoothSDB -> Smoothing surface with various algorithm.
    			VDBCombine -> Boolean operation
    			Houdini standard volume has exclusive toolset/openCL function.
    		Volume boolean
    			Volume modeling
    				Voxel size decrease to half of the smallest feature of geometry.        
        # VDB_VectorField
            SDF collision
    def POP
        
    def DOP
class FX_Dev
    Mindset = hard coded vs tool usage
	def Growth
    # 1 way transform.
        Copy&Instance
            #Dev_Crassula
        Noise + @P transform
            #Dev_SnakeIsland
        Move & Trail
            #Project_NikeFlyknit
        VDB modeling/advecting
            #Dev_Organic
    def Morph
    # 2 ways transform.          
        UV xform 
                #Dev_LineMorph
                #Dev_Venus
        @P mix function
            #Dev_Knitting
    def Magic
        Vector field Vel & SDF
            #Dev_MagicFluid
        POP Force
            #Dev_Cradence

class FX_Project
    def FxBorg
        Create FxBorg with dev effects.
            3D model rigging/animating
            FX develop
            Rendering(Houdini x Redshift)
            Compositing(Fusion)
            Color grading(Resolve)
            Camera tracking(Fusion)
        # fxb_1
            # FxBorg Arm replacemnt
                # -Watercooling tube
                    # Straight/Curl
                # -Wireframe mechanic
                # -Lab particles test tube
                ##-Crawling mamba mechanic
                
