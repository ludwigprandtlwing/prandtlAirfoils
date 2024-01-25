function skryf_vlerkprofiel_uit(leernaam, vlerkprofielnaam, x, y)

% LEES_VLERKPROFIEL Lees 'n XFOIL *.dat lêer in 'n x en y skikking in

% Lees die inhoud van die lêer
fid = fopen(leernaam, 'w');

% Skryf die vlerkprofiel se naam in
fprintf(fid, vlerkprofielnaam);
fprintf(fid, '\n');

for lynteller = 1:size(x, 2)  
    fprintf(fid, '%6.5f %6.5f\n', x(lynteller), y(lynteller));   
end

fclose(fid);