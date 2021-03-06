# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..brainsresample import BRAINSResample


def test_BRAINSResample_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        defaultValue=dict(argstr='--defaultValue %f', ),
        deformationVolume=dict(argstr='--deformationVolume %s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        gridSpacing=dict(
            argstr='--gridSpacing %s',
            sep=',',
        ),
        ignore_exception=dict(
            deprecated='1.0.0',
            nohash=True,
            usedefault=True,
        ),
        inputVolume=dict(argstr='--inputVolume %s', ),
        interpolationMode=dict(argstr='--interpolationMode %s', ),
        inverseTransform=dict(argstr='--inverseTransform ', ),
        numberOfThreads=dict(argstr='--numberOfThreads %d', ),
        outputVolume=dict(
            argstr='--outputVolume %s',
            hash_files=False,
        ),
        pixelType=dict(argstr='--pixelType %s', ),
        referenceVolume=dict(argstr='--referenceVolume %s', ),
        terminal_output=dict(
            deprecated='1.0.0',
            nohash=True,
        ),
        warpTransform=dict(argstr='--warpTransform %s', ),
    )
    inputs = BRAINSResample.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_BRAINSResample_outputs():
    output_map = dict(outputVolume=dict(), )
    outputs = BRAINSResample.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
