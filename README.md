# Annotate Mutation On trees

To annotate mutations on tree nodes and tips, input files include translated amino acid sequences and newick trees

Ancestral sequence reconstruction
```
treetime ancestral --aln .\Seq.translated.fas --tree .\Seqtree.nwk --aa --outdir ./ancestral
```

TreeTime will generate a folder named ancestral, containing ancestral sequences and annotated nexus tree.

Mutations are stored in \[&mutations="S1G,S2T"\]. Can view the mutation in Figtree directly.
Convert this to old view with Node000@S1G@S2T
```
python convert.py .\ancestral\annotated_tree.nexus H3_ancestral_label.nwk
```
