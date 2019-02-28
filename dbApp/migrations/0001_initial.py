# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-02-27 23:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnalysisGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AnalysisType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_footprint_list', models.CharField(max_length=200, null=True)),
                ('majority_reference_sequence_set', models.CharField(max_length=40, null=True)),
                ('list_of_clade_collections_found_in_initially', models.CharField(max_length=5000, null=True)),
                ('list_of_clade_collections', models.CharField(max_length=100000, null=True)),
                ('footprint_sequence_abundances', models.CharField(max_length=100000, null=True)),
                ('footprint_sequence_ratios', models.CharField(max_length=100000, null=True)),
                ('clade', models.CharField(max_length=1)),
                ('co_dominant', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=1000, null=True)),
                ('max_min_ratios', models.CharField(max_length=100000, null=True)),
                ('species', models.CharField(max_length=200, null=True)),
                ('artefact_intras', models.CharField(default='', max_length=5000)),
                ('is_locked_type', models.BooleanField(default=False)),
                ('basal_seq', models.CharField(default=None, max_length=10, null=True)),
                ('analysis_group_of', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dbApp.AnalysisGroup')),
            ],
        ),
        migrations.CreateModel(
            name='CladeCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clade', models.CharField(max_length=1)),
                ('footprint', models.CharField(default=True, max_length=100000)),
            ],
        ),
        migrations.CreateModel(
            name='CladeCollectionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('analysis_type_of', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dbApp.AnalysisType')),
                ('clade_collection_found_in', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dbApp.CladeCollection')),
            ],
        ),
        migrations.CreateModel(
            name='DataAnalysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_of_data_set_uids', models.CharField(max_length=500, null=True)),
                ('within_clade_cutoff', models.FloatField(default=0.04)),
                ('type_support', models.FloatField(default=0.01)),
                ('clade_collection_population_complete', models.BooleanField(default=False)),
                ('analysis_types_defined', models.BooleanField(default=False)),
                ('initial_type_discovery_complete', models.BooleanField(default=False)),
                ('analysis_types_assigned', models.BooleanField(default=False)),
                ('analysis_types_collapsed', models.BooleanField(default=False)),
                ('reference_sequences_named', models.BooleanField(default=False)),
                ('species_associated', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=5000, null=True)),
                ('time_stamp', models.CharField(default='None', max_length=100)),
                ('submitting_user', models.CharField(default='no_user_defined', max_length=100)),
                ('submitting_user_email', models.CharField(default='no_email_defined', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='something', max_length=60)),
                ('reference_fasta_database_used', models.CharField(default='None', max_length=60)),
                ('submitting_user', models.CharField(default='no_user_defined', max_length=100)),
                ('submitting_user_email', models.CharField(default='no_email_defined', max_length=100)),
                ('working_directory', models.CharField(default='None', max_length=300)),
                ('data_processed', models.BooleanField(default=False)),
                ('initial_data_processed', models.BooleanField(default=False)),
                ('currently_being_processed', models.BooleanField(default=False)),
                ('time_stamp', models.CharField(default='None', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DataSetSample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='None', max_length=200)),
                ('num_contigs', models.IntegerField(default=0)),
                ('post_qc_absolute_num_seqs', models.IntegerField(default=0)),
                ('post_qc_unique_num_seqs', models.IntegerField(default=0)),
                ('absolute_num_sym_seqs', models.IntegerField(default=0)),
                ('unique_num_sym_seqs', models.IntegerField(default=0)),
                ('non_sym_absolute_num_seqs', models.IntegerField(default=0)),
                ('non_sym_unique_num_seqs', models.IntegerField(default=0)),
                ('size_violation_absolute', models.IntegerField(default=0)),
                ('size_violation_unique', models.IntegerField(default=0)),
                ('post_med_absolute', models.IntegerField(default=0)),
                ('post_med_unique', models.IntegerField(default=0)),
                ('initial_processing_complete', models.BooleanField(default=False)),
                ('final_processing_complete', models.BooleanField(default=False)),
                ('error_in_processing', models.BooleanField(default=False)),
                ('error_reason', models.CharField(default='noError', max_length=100)),
                ('cladal_seq_totals', models.CharField(max_length=5000, null=True)),
                ('sample_type', models.CharField(default='NoData', max_length=50)),
                ('host_phylum', models.CharField(default='NoData', max_length=50)),
                ('host_class', models.CharField(default='NoData', max_length=50)),
                ('host_order', models.CharField(default='NoData', max_length=50)),
                ('host_family', models.CharField(default='NoData', max_length=50)),
                ('host_genus', models.CharField(default='NoData', max_length=50)),
                ('host_species', models.CharField(default='NoData', max_length=50)),
                ('collection_latitude', models.DecimalField(decimal_places=8, default=999.99999999, max_digits=11)),
                ('collection_longitude', models.DecimalField(decimal_places=8, default=999.99999999, max_digits=11)),
                ('collection_date', models.CharField(default='NoData', max_length=40)),
                ('collection_depth', models.CharField(default='NoData', max_length=40)),
                ('data_submission_from', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dbApp.DataSet')),
            ],
        ),
        migrations.CreateModel(
            name='DataSetSampleSequence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abundance', models.IntegerField(default=0)),
                ('clade_collection_found_in', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dbApp.CladeCollection')),
                ('data_set_sample_from', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dbApp.DataSetSample')),
            ],
        ),
        migrations.CreateModel(
            name='ReferenceSequence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='noName', max_length=30)),
                ('has_name', models.BooleanField(default=False)),
                ('clade', models.CharField(max_length=30)),
                ('sequence', models.CharField(max_length=500)),
                ('accession', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SymportalFramework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latest_reference_fasta', models.CharField(default='symClade_2_2.fa', max_length=30)),
                ('next_reference_fasta_iteration', models.IntegerField(default=1)),
                ('required_sub_e_value_seq_support_samples', models.IntegerField(default=3)),
                ('required_sub_e_value_seq_support_blast_symbiodinium', models.IntegerField(null=2)),
            ],
        ),
        migrations.AddField(
            model_name='datasetsamplesequence',
            name='reference_sequence_of',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dbApp.ReferenceSequence'),
        ),
        migrations.AddField(
            model_name='cladecollection',
            name='data_set_sample_from',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dbApp.DataSetSample'),
        ),
        migrations.AddField(
            model_name='analysistype',
            name='data_analysis_from',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dbApp.DataAnalysis'),
        ),
        migrations.AddField(
            model_name='analysisgroup',
            name='data_analysis_from',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dbApp.DataAnalysis'),
        ),
    ]
