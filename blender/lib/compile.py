#!/usr/bin/python

# Usage: 'python compile.py'
# Output ../compiled/

import make_resources
import make_variants
import os

os.chdir('./forward')
make_resources.make('forward.shader.json')
make_variants.make('forward.shader.json')

os.chdir('../deferred')
make_resources.make('deferred.shader.json')
make_variants.make('deferred.shader.json')

os.chdir('../deferred_light')
make_resources.make('deferred_light.shader.json')
make_variants.make('deferred_light.shader.json')

os.chdir('../env_map')
make_resources.make('env_map.shader.json')
make_variants.make('env_map.shader.json')

os.chdir('../fxaa_pass')
make_resources.make('fxaa_pass.shader.json')
make_variants.make('fxaa_pass.shader.json')

os.chdir('../ssao_pass')
make_resources.make('ssao_pass.shader.json')
make_variants.make('ssao_pass.shader.json')

os.chdir('../ssdo_pass')
make_resources.make('ssdo_pass.shader.json')
make_variants.make('ssdo_pass.shader.json')

os.chdir('../blur_pass')
make_resources.make('blur_pass.shader.json')
make_variants.make('blur_pass.shader.json')

os.chdir('../motion_blur_pass')
make_resources.make('motion_blur_pass.shader.json')
make_variants.make('motion_blur_pass.shader.json')

os.chdir('../compositor_pass')
make_resources.make('compositor_pass.shader.json')
make_variants.make('compositor_pass.shader.json')

os.chdir('../bloom_pass')
make_resources.make('bloom_pass.shader.json')
make_variants.make('bloom_pass.shader.json')

os.chdir('../ssr_pass')
make_resources.make('ssr_pass.shader.json')
make_variants.make('ssr_pass.shader.json')

os.chdir('../combine_pass')
make_resources.make('combine_pass.shader.json')
make_variants.make('combine_pass.shader.json')

os.chdir('../sss_pass')
make_resources.make('sss_pass.shader.json')
make_variants.make('sss_pass.shader.json')

os.chdir('../water_pass')
make_resources.make('water_pass.shader.json')
make_variants.make('water_pass.shader.json')

os.chdir('../godrays_pass')
make_resources.make('godrays_pass.shader.json')
make_variants.make('godrays_pass.shader.json')

# os.chdir('../pt_trace_pass')
# make_resources.make('pt_trace_pass.shader.json')
# make_variants.make('pt_trace_pass.shader.json')

# os.chdir('../pt_final_pass')
# make_resources.make('pt_final_pass.shader.json')
# make_variants.make('pt_final_pass.shader.json')
