from pyknow import *

class AcornFinder(KnowledgeEngine):
    """Acorn expert system"""

    # questions
    @Rule(
          NOT(Fact(cap=W()))
    )
    def _ask_cap(self):
        self.declare(Fact(cap=input("What type of cap? (STRIPED, SCALED, TULIP, PRICKLY): ")))
        
    @Rule(
         AND(
            Fact(cap='STRIPED')
        )
    )
    def _ask_head(self):
        self.declare(Fact(head=input("Head stands out? (YES, NO): ")))

    @Rule(
        AND(
            Fact(cap='SCALED')
        )
    )
    def _ask_indent(self):
        self.declare(Fact(indented=input("Indented under the cap? (YES, NO): ")))

    @Rule(
        OR(
            AND(
                Fact(cap='SCALED'),
                Fact(indented='YES')
            ),
            AND(
                Fact(cap='TULIP')
            )
        )

    )
    def _ask_shape(self):
        self.declare(Fact(shape=input("Shape of acorn? (ROUND, LONG, TRIANGLE): ")))

    @Rule(
        AND(
            Fact(cap='SCALED'),
            Fact(indented='NO')
        )
    )
    def _ask_scale_size(self):
        self.declare(Fact(scale_size=input("Scale size? (BIG, SMALL): ")))

    @Rule(
        AND(
            Fact(cap='TULIP'),
            Fact(shape='TRIANGLE')
        )
    )
    def _ask_cap_pattern(self):
        self.declare(Fact(cap_pattern=input("Cap pattern? (LONG, SHORT): ")))

    @Rule(
        Fact(cap='PRICKLY'),
    )
    def _ask_spike_shape(self):
        self.declare(Fact(spike_shape=input("Shape of spikes? (THICK, THIN, NEEDLE): ")))


    # answers
    @Rule(
        AND(
            Fact(cap='STRIPED'),
            Fact(head='YES')
        )
    )
    def _id_quercus_gilva(self):
        print("Quercus gilva")

    @Rule(
        AND(
            Fact(cap='STRIPED'),
            Fact(head='NO')
        )
    )
    def _id_quercus_myrsinifolia(self):
        print("Quercus myrsinifolia")

    @Rule(
        AND(
            Fact(cap='SCALED'),
            Fact(indented='YES'),
            Fact(shape='ROUND')
        )
    )
    def _id_lithocarpus_glaber(self):
        print("Lithocarpus glaber​")

    @Rule(
        AND(
            Fact(cap='SCALED'),
            Fact(indented='YES'),
            Fact(shape='LONG')
        )
    )
    def _id_lithocarpus_edulis(self):
        print("Lithocarpus edulis​")

    @Rule(
        AND(
            Fact(cap='SCALED'),
            Fact(indented='NO'),
            Fact(scale_size='SMALL')
        )
    )
    def _id_quercus_serrata(self):
        print("Quercus serrata")

    @Rule(
        AND(
            Fact(cap='SCALED'),
            Fact(indented='NO'),
            Fact(scale_size='BIG')
        )
    )
    def _id_quercus_aliena(self):
        print("Quercus aliena")

    @Rule(
        AND(
            Fact(cap='TULIP'),
            Fact(shape='ROUND')
        )
    )
    def _id_castanopsis_cuspidata(self):
        print("Castanopsis cuspidata")

    @Rule(
        AND(
            Fact(cap='TULIP'),
            Fact(shape='LONG')
        )
    )
    def _id_castanopsis_sieboldii(self):
        print("Castanopsis sieboldii")

    @Rule(
        AND(
            Fact(cap='TULIP'),
            Fact(shape='TRIANGLE'),
            Fact(cap_pattern='SHORT')
        )
    )
    def _id_fagus_crenata(self):
        print("Fagus crenata")

    @Rule(
        AND(
            Fact(cap='TULIP'),
            Fact(shape='TRIANGLE'),
            Fact(cap_pattern='LONG')
        )
    )
    def _id_fagus_japonica(self):
        print("Fagus japonica")

    @Rule(
        AND(
            Fact(cap='PRICKLY'),
            Fact(spike_shape='THICK')
        )
    )
    def _id_quercus_acutissima(self):
        print("Quercus acutissima")
        
    @Rule(
        AND(
            Fact(cap='PRICKLY'),
            Fact(spike_shape='THIN')
        )
    )
    def _id_quercus_dentata(self):
        print("Quercus dentata​")

    @Rule(
        AND(
            Fact(cap='PRICKLY'),
            Fact(spike_shape='NEEDLE')
        )
    )
    def _id_castanea_crenata(self):
        print("Castanea crenata")

    @Rule(
    )
    def _end(self):
        print("END")
        
    
        
engine = AcornFinder()
engine.reset()
engine.run()
