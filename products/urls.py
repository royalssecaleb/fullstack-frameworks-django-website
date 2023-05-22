# Products related urls
from django.conf.urls import url, include
from products.views import products, alt_dyno, body, bonnet, boot, brakes, brakes_fr, brakes_handbrake, bumpers, \
                           chassis, clutch, cooling, crankshaft, dashboard, door, drive_line, electrical, engine, exhaust, external, \
                           fuel, fuel_pipes, fuel_tank, gearbox, gearbox_mk4, gearbox_1500, hardtop, heating, hood, \
                           ignition, inner_body, inst_sw, interior, lamps, mouldings, oilsump, outer_body, overdrive, \
                           overdrive_j, rad_grill, ratings, road_wheels, seats, steering, suspension, trim_kits, windscreen, wshld_wipe_wash, wire_int
                              
urlpatterns = [
    url(r'^categories/$', products, name='products'),
    url(r'^alt_dyno/$', alt_dyno, name='alt_dyno'),
    url(r'^body/$', body, name='body'),
    url(r'^bonnet/$', bonnet, name='bonnet'),
    url(r'^boot/$', boot, name='boot'),
    url(r'^brakes/$', brakes, name='brakes'),
    url(r'^brakes_fr/$', brakes_fr, name='brakes_fr'),
    url(r'^brakes_handbrake/$', brakes_handbrake, name='brakes_handbrake'),
    url(r'^bumpers/$', bumpers, name='bumpers'),
    url(r'^chassis/$', chassis, name='chassis'),
    url(r'^clutch/$', clutch, name='clutch'),
    url(r'^cooling/$', cooling, name='cooling'),
    url(r'^crankshaft/$', crankshaft, name='crankshaft'),
    url(r'^dashboard/$', dashboard, name='dashboard'),
    url(r'^door/$', door, name='door'),
    url(r'^drive_line/$', drive_line, name='drive_line'),
    url(r'^electrical/$', electrical, name='electrical'), 
    url(r'^engine/$', engine, name='engine'),
    url(r'^exhaust/$', exhaust, name='exhaust'),
    url(r'^external/$', external, name='external'),
    url(r'^fuel/$', fuel, name='fuel'),
    url(r'^fuel_pipes/$', fuel_pipes, name='fuel_pipes'),
    url(r'^fuel_tank/$', fuel_tank, name='fuel_tank'),
    url(r'^gearbox/$', gearbox, name='gearbox'),
    url(r'^gearbox_mk4/$', gearbox_mk4, name='gearbox_mk4'),
    url(r'^gearbox_1500/$', gearbox_1500, name='gearbox_1500'),
    url(r'^hardtop/$', hardtop, name='hardtop'),
    url(r'^heating/$', heating, name='heating'),
    url(r'^hood/$',hood, name='hood'),
    url(r'^ignition/$', ignition, name='ignition'),
    url(r'^inner_body/$', inner_body, name='inner_body'),
    url(r'^inst_sw/$', inst_sw, name='inst_sw'),
    url(r'^interior/$', interior, name='interior'),
    url(r'^lamps/$', lamps, name='lamps'),
    url(r'^mouldings/$', mouldings, name='mouldings'),
    url(r'^oilsump/$', oilsump, name='oilsump'),
    url(r'^overdrive/$', overdrive, name='overdrive'),
    url(r'^overdrive_j/$', overdrive_j, name='overdrive_j'),
    url(r'^outer_body/$', outer_body, name='outer_body'),
    url(r'^rad_grill/$', rad_grill, name='rad_grill'),
    url(r'^ratings/$', ratings, name='ratings'),
    url(r'^road_wheels/$', road_wheels, name='road_wheels'),
    url(r'^seats/$', seats, name='seats'),
    url(r'^steering/$', steering, name='steering'),
    url(r'^suspension/$', suspension, name='suspension'),
    url(r'^trim_kits/$', trim_kits, name='trim_kits'),
    url(r'^wshld_wipe_wash/$', wshld_wipe_wash, name='wshld_wipe_wash'),
    url(r'^windscreen/$', windscreen, name='windscreen'),
    url(r'^wire_int/$', wire_int, name='wire_int'),
]  