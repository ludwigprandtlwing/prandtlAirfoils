function [x, y] = lees_vlerkprofiel_in(leernaam)

% LEES_VLERKPROFIEL Lees 'n XFOIL *.dat lêer in 'n x en y skikking in

% Lees die inhoud van die lêer
fid = fopen(leernaam);
lynteller = 0;

while 1
    leerlyn = fgetl(fid);
    lynteller = lynteller + 1;
    if ~ischar(leerlyn), break, end
    
    % Skryf die waardes in 'n skikking
    if lynteller > 1
        x_y = str2num(leerlyn);
        x(1, lynteller - 1) = x_y(1);
        y(1, lynteller - 1) = x_y(2);
    end   
end

fclose(fid);