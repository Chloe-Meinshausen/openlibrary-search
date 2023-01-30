--  you can either run from the terminal or paste into the query tool in Pgadmin.
DO
$do$
declare

     filepath varchar 'add your filepath here'
    input_filename varchar;
    final_filename varchar;
    -- rename  to match proper table
	name_of_table varchar := 'authors';
    cnt integer := 1 ;
    -- use the data printed in the console when you split your files to fill this array.
    input_filenames varchar[] := array['author_3000000.csv', 'author_6000000.csv', 'author_9000000.csv', 'author_12000000.csv'];
begin
	raise notice 'beginning process...';
    foreach input_filename in array input_filenames
    loop
        final_filename := concat(filepath , input_filename);
        execute format('COPY %s FROM  %L DELIMITER %L QUOTE E%L CSV', name_of_table, final_filename, E'\t','|');
		raise notice 'completed file % of %', cnt, cardinality(input_filenames);
        cnt := cnt + 1 ;
    end loop;
end
$do$
