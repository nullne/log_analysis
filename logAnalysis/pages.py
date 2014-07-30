#!/usr/bin/env python
def main():
    res = {
            'root': {
                '/': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/',
                    'get_params': [
                        ],
                    },
                'accounts_login': {
                    'type': 'GET',
                    'url_pattern': '/accounts/login',
                    'get_params': [
                        ],
                    },
                },
            'TestPlan LoadMoreCases': {
                'cases_loadmore': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/cases/load-more',
                    'get_params': [
                        ],
                    },
                },
            'Test Plan Reviewing cases': {
                'cases': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/cases',
                    'get_params': [
                        'a=initial',
                        'template_type=review_case',
                        ],
                    },
                },
            'TestPlan_LoadMoreReviewingCases': {
                'cases_load-more': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/cases/load-more',
                    'get_params': [
                        ],
                    },
                },
            'TestPlan_DefaultComponent_Update': {
                'plans_componentst': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/plans/component',
                    'get_params': [
                        'a=get_form',
                        ],
                    },
                },
            'TestPlan_DefaultComponent_Commit': {
                'plans_components': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/plans/component',
                    'get_params': [
                        'a=Update'
                        ],
                    },
                },
            'TestPlan_DefaultComponent_Remove': {
                'plans_componets': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/plans/component',
                    'get_params': [
                        'a=remove',
                        ],
                    },
                },
            'TestPlan_Attachment_Add': {
                '/plan/6381/attachment/': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/plan/idnumber/attachment',
                    'get_params': [
                        ],
                    },
                },
            'TestPlan_Attachment_Upload': {
                '/management/uploadfile/': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/management/uploadfile',
                    'get_params': [
                        ],
                    },
                '/plan/planid/attachment/': {
                    'type': 'GET',
                    'url_pattern': '/plan/idnumber/attachment/',
                    'get_params': [
                        ],
                    },
                },
            'TestPlan_Attachment_Delete': {
                '/management/deletefile/checkfileid': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/management/deletefile/idnumber',
                    'get_params': [
                        ],
                    },
                },
            'TestPlan_Tags_Add': {
                '/management/tags': {
                    'type': 'GET',
                    'main': True,
                    'url_pattern': '/management/tags',
                    'get_params': [
                        'a=add',
                        ],
                    },
                },
            'TestPlan_Tags_Update': {
                '/management/tagsadd/': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/management/tags',
                    'get_params': [
                        'a=add'
                        ],
                    },
                '/management/tags/': {
                    'type': 'GET',
                    'url_pattern': '/management/tags',
                    'get_params': [
                        'a=remove',
                        ],
                    },
                },
            'TestPlan_Tags_Remove': {
                '/management/tags/': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/management/tags',
                    'get_params': [
                        'a=remove'
                        ],
                    },
                },
            'TestPlan_TreeView': {
                '/plans/': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/plans',
                    'get_params': [
                        't=ajax'
                        ],
                    },
                '/planss/': {
                    'type': 'GET',
                    'url_pattern': '/plans',
                    'get_params': [
                        't=ajax'
                        ],
                    },
                },
            'TestPlan_TreeView_ChangeParent': {
                '/ajax/update/': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/ajax/update',
                    'get_params': [
                        'content_type=testplans.testplan',
                        'field=parent',
                        ],
                    },
                '/plans/': {
                    'type': 'GET',
                    'url_pattern': '/plans',
                    'get_params': [
                        't=ajax'
                        ],
                    },
                },
            'TestPlan_TreeView_AddChildNode': {
                '/ajax/update/': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/ajax/update',
                    'get_params': [
                        'content_type=testplans.testplan',
                        'field=parent',
                        'value_type=int'
                        ],
                    },
                '/plans/': {
                    'type': 'GET',
                    'url_pattern': '/plans',
                    'get_params': [
                        't=ajax'
                        ],
                    },
                '/plans/': {
                    'type': 'GET',
                    'url_pattern': '/plans',
                    'get_params': [
                        't=ajax'
                        ],
                    },
                },
            'TestPlan_TreeView_RemoveChildNode': {
                '/ajax/update/': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/ajax/update',
                    'get_params': [
                        'content_type=testplans.testplan',
                        'field=parent',
                        'value_type=None'
                        ],
                    },
                '/plans/': {
                    'type': 'GET',
                    'url_pattern': '/plans',
                    'get_params': [
                        't=ajax'
                        ],
                    },
                '/plans/': {
                    'type': 'GET',
                    'url_pattern': '/plans',
                    'get_params': [
                        't=ajax'
                        ],
                    },
                },
            'TestPlan_Runs': {
                '/plan/planid/runs/': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/plan/idnumber/runs',
                    'get_params': [
                        ],
                    },
                },
            'TestPlan_MyPlan': {
                '/plans': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/plans',
                    'get_params': [
                        ],
                    },
                '/admin/jsi18n/': {
                    'type': 'GET',
                    'url_pattern': '/admin/jsi18n',
                    'get_params': [
                        ],
                    },
                '/plans/ajax/': {
                    'type': 'GET',
                    'url_pattern': '/plans/ajax',
                    'get_params': [
                        ],
                    },
                },
            'TestPlan_Edit': {
                '/plan/idnumber/edit': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/plan/idnumber/edit',
                    'get_params': [
                        ],
                    },
                },
            'TestPlan_EditSave': {
                '/plan/6381/edit': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/plan/idnumber/edit',
                    'get_params': [
                        ],
                    },
                '/plan/idnumber/planName': {
                    'type': 'GET',
                    'url_pattern': '/plan/idnumber/planName',
                    'get_params': [
                        ],
                    },
                '/management/tags/': {
                    'type': 'GET',
                    'url_pattern': '/management/tags',
                    'get_params': [
                        ],
                    },
                '/plans/component/': {
                    'type': 'GET',
                    'url_pattern': '/plans/component',
                    'get_params': [
                        ],
                    },
		#   % -- not uesd
                '%/admin/jsi18n/': {
                    'type': 'GET',
                    'url_pattern': '/admin/jsi18',
                    'get_params': [
                        ],
                    },
                '/cases/': {
                    'type': 'POST',
                    'url_pattern': '/cases',
                    'get_params': [
                        ],
                    },
                },
            'TestPlan_New': {
                '/plan/new': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/plan/new',
                    'get_params': [
                        ],
                    },
                '/management/getinfo/': {
                    'type': 'GET',
                    'url_pattern': '/management/getinfo',
                    'get_params': [
                        'info_type=versions',
                        ],
                    },
                },
            'TestPlan_Save': {
                '/plan/new': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/plan/new',
                    'get_params': [
                        ],
                    },
                '/management/tags/': {
                    'type': 'GET',
                    'url_pattern': '/management/tags',
                    'get_params': [
                        ],
                    },
                '/plans/component/': {
                    'type': 'GET',
                    'url_pattern': '/plans/component',
                    'get_params': [
                        ],
                    },
                '/admin/jsi18n/': {
                    'type': 'GET',
                    'url_pattern': '/admin/jsi18n',
                    'get_params': [
                        ],
                    },
                '/cases/': {
                    'type': 'POST',
                    'url_pattern': '/cases',
                    'get_params': [
                        ],
                    },
                },
            'TestPlan_Clone': {
                '/plans/clone': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/plans/clone',
                    'get_params': [
                        ],
                    },
                },
            'TestPlan_CloneSave': {
                '/plans/clone': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/plans/clone',
                    'get_params': [
                        ],
                    },
                '/management/tags/': {
                    'type': 'GET',
                    'url_pattern': '/management/tags',
                    'get_params': [
                        ],
                    },
                '/plans/component/': {
                    'type': 'GET',
                    'url_pattern': '/plans/component',
                    'get_params': [
                        ],
                    },
                '/admin/jsi18n/': {
                    'type': 'GET',
                    'url_pattern': '/admin/jsi18n',
                    'get_params': [
                        ],
                    },
                '/cases/': {
                    'type': 'POST',
                    'url_pattern': '/cases',
                    'get_params': [
                        ],
                    },
                },
            'TestPlan_Clone_100cases': {
                '/plans/clone': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/plans/clone',
                    'get_params': [
                        ],
                    },
                },
            'TestPlan_CloneSave_100cases': {
                '/plans/clone': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/plans/clone',
                    'get_params': [
                        ],
                    },
                '/management/tags': {
                    'type': 'GET',
                    'url_pattern': '/management/tags',
                    'get_params': [
                        ],
                    },
                '/plans/component/': {
                    'type': 'GET',
                    'url_pattern': '/plans/component',
                    'get_params': [
                        ],
                    },
                '/admin/jsi18n': {
                    'type': 'GET',
                    'url_pattern': '/admin/jsi18n',
                    'get_params': [
                        ],
                    },
                '/cases': {
                    'type': 'POST',
                    'url_pattern': '/cases',
                    'get_params': [
                        ],
                    },
                },
            'TestPlan_DisablePlan': {
                '/ajax/update': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/ajax/update',
                    'get_params': [
                        ],
                    },
                '/plan/idnumber': {
                    'type': 'GET',
                    'url_pattern': '/plan/idnumber',
                    'get_params': [
                        ],
                    },
                '/plan/idnumber/planname': {
                    'type': 'GET',
                    'url_pattern': '/plan/idnumber/planName',
                    'get_params': [
                        ],
                    },
                '/management/tags': {
                    'type': 'GET',
                    'url_pattern': '/management/tags',
                    'get_params': [
                        ],
                    },
                '/plans/component/': {
                    'type': 'GET',
                    'url_pattern': '/plans/component',
                    'get_params': [
                        ],
                    },
                '/admin/jsi18n': {
                    'type': 'GET',
                    'url_pattern': '/admin/jsi18n',
                    'get_params': [
                        ],
                    },
                '/cases': {
                    'type': 'POST',
                    'url_pattern': '/cases',
                    'get_params': [
                        ],
                    },
                },
            'TestPlan_EnablePlan': {
                '/ajax/update': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/ajax/update',
                    'get_params': [
                        ],
                    },
                '/plan/idnumber': {
                    'type': 'GET',
                    'url_pattern': '/plan/idnumber',
                    'get_params': [
                        ],
                    },
                '/plan/idnumber/planname': {
                    'type': 'GET',
                    'url_pattern': '/plan/idnumber/planName',
                    'get_params': [
                        ],
                    },
                '/management/tags': {
                    'type': 'GET',
                    'url_pattern': '/management/tags',
                    'get_params': [
                        ],
                    },
                '/plans/component/': {
                    'type': 'GET',
                    'url_pattern': '/plans/component',
                    'get_params': [
                        ],
                    },
                '/admin/jsi18n': {
                    'type': 'GET',
                    'url_pattern': '/admin/jsi18n',
                    'get_params': [
                        ],
                    },
                '/cases': {
                    'type': 'POST',
                    'url_pattern': '/cases',
                    'get_params': [
                        ],
                    },
                },
            'TestPlan_Printable': {
                '/cases/printable': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/cases/printable',
                    'get_params': [
                        ],
                    },
                },
            '@TestPlan_Printable_100cases': {
                '/cases/printable': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/cases/printable',
                    'get_params': [
                        ],
                    },
                },
            'TestPlan_ExportAllCases': {
                '/cases/export/': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/cases/export',
                    'get_params': [
                        ],
                    },
                },
            '@TestPlan_Cases_Filter': {
                '/cases': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/cases',
                    'get_params': [
                        ],
                    },
                },
            'TestPlan_Cases_Expand': {
                '/cases/caseid': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/cases/idnumber',
                    'get_params': [
			'template_type=case',
                        ],
                    },
                },
            'TestPlan_Cases_Case_ImportCaseFromXML': {
                '/plan/6381/cases': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/plan/idnumber/cases',
                    'get_params': [
                        ],
                    },
                'plan_planid': {
                    'type': 'GET',
                    'url_pattern': '/plan/dnumber/planName',
                    'get_params': [
                        ],
                    },
                'plan_id': {
                    'type': 'GET',
                    'url_pattern': '/plan/idnumber',
                    'get_params': [
                        ],
                    },
                'management_tags': {
                    'type': 'GET',
                    'url_pattern': '/management/tags',
                    'get_params': [
                        ],
                    },
                'plans_component': {
                    'type': 'GET',
                    'url_pattern': '/plans/component',
                    'get_params': [
                        ],
                    },
                'admins_jsi18n': {
                    'type': 'GET',
                    'url_pattern': '/admin/jsi18n',
                    'get_params': [
                        ],
                    },
                'cases': {
                    'type': 'POST',
                    'url_pattern': '/cases',
                    'get_params': [
                        ],
                    },
                },
            'TestPlan_Cases_Case_Remove': {
                '/plan/planid/cases/': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/plan/idnumber/cases',
                    'get_params': [
                        ],
                    },
                '/cases': {
                    'type': 'POST',
                    'url_pattern': '/cases',
                    'get_params': [
                        ],
                    },
                },
            '#TestPlan_Cases_Case_AddCaseFromOtherPlan': {
                '/plan/planid/cases': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/plan/idnumber/cases',
                    'get_params': [
			'a=link_cases'
                        ],
                    },
                '/management/getinfo/': {
                    'type': 'GET',
                    'url_pattern': '/management/getinfo',
                    'get_params': [
			'info_type=categories',
                        ],
                    },
                '/management/getinfo': {
                    'type': 'GET',
                    'url_pattern': '/management/getinfo',
                    'get_params': [
			'info_type=components',
                        ],
                    },
                },
            'TestPlan_Cases_Case_AddCaseFromOtherPlan_Search': {
                '/plan/idnumber/cases': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/plan/idnumber/cases',
                    'get_params': [
                        ],
                    },
                '/management/getinfo/': {
                    'type': 'GET',
                    'url_pattern': '/management/getinfo',
                    'get_params': [
			'info_type=categories',
                        ],
                    },
                '/management/getinfo': {
                    'type': 'GET',
                    'url_pattern': '/management/getinfo',
                    'get_params': [
			'info_type=components',
                        ],
                    },
                },
            'TestPlan_Cases_Case_AddCaseFromOtherPlan_AddSelectCases': {
                '/plan/idnumber/cases': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/plan/idnumber/cases',
                    'get_params': [
                        ],
                    },
                'plan_planid': {
                    'type': 'GET',
                    'url_pattern': '/plan/idnumber/planName',
                    'get_params': [
                        ],
                    },
                'plan_id': {
                    'type': 'GET',
                    'url_pattern': '/plan/idnumber',
                    'get_params': [
                        ],
                    },
                'management_tags': {
                    'type': 'GET',
                    'url_pattern': '/management/tags',
                    'get_params': [
                        ],
                    },
                'plans_component': {
                    'type': 'GET',
                    'url_pattern': '/plans/component',
                    'get_params': [
                        ],
                    },
                'admins_jsi18n': {
                    'type': 'GET',
                    'url_pattern': '/admin/jsi18n',
                    'get_params': [
                        ],
                    },
                'cases': {
                    'type': 'POST',
                    'url_pattern': '/cases',
                    'get_params': [
                        ],
                    },
                },
            '@TestPlan_Cases_Case_ClonePage': {
                '/cases/clone': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/cases/clone',
                    'get_params': [
			'type=case',
                        ],
                    },
                },
            'TestPlan_Cases_Case_CloneFilter': {
                '/plans': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/plans',
                    'get_params': [
			'action=clone_case'
                        ],
                    },
                },
            'TestPlan_Cases_Case_Clone': {
                '/cases/clone': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/cases/clone',
                    'get_params': [
                        ],
                    },
                'management_tags': {
                    'type': 'GET',
                    'url_pattern': '/management/tags',
                    'get_params': [
                        ],
                    },
                'plans_component': {
                    'type': 'GET',
                    'url_pattern': '/plans/component',
                    'get_params': [
                        ],
                    },
                'admins_jsi18n': {
                    'type': 'GET',
                    'url_pattern': '/admin/jsi18n',
                    'get_params': [
                        ],
                    },
                'cases': {
                    'type': 'POST',
                    'url_pattern': '/cases',
                    'get_params': [
                        ],
                    },
                },
            'TestPlan_Cases_Case_SetSortNumber': {
                '/ajax/update': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/ajax/update',
                    'get_params': [
                        ],
                    },
                '/cases': {
                    'type': 'POST',
                    'url_pattern': '/cases',
                    'get_params': [
                        ],
                    },
                },
            'TestPlan_Cases_Case_Export': {
                '/cases/export': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/cases/export',
                    'get_params': [
                        ],
                    },
                },
            'TestPlan_Cases_Case_WriteNew': {
                '/case/new': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/case/new',
                    'get_params': [
                        ],
                    },
                '/admin/jsi18n': {
                    'type': 'GET',
                    'url_pattern': '/admin/jsi18n',
                    'get_params': [
                        ],
                    },
                },
            'TestPlan_Cases_Case_Save': {
                '/case/new': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/case/new',
                    'get_params': [
                        ],
                    },
                '/management/tags': {
                    'type': 'GET',
                    'url_pattern': '/management/tags',
                    'get_params': [
                        ],
                    },
                '/case/idnumber/plan': {
                    'type': 'GET',
                    'url_pattern': '/case/idnumber/plan',
                    'get_params': [
                        ],
                    },
                },
            'TestPlan_Cases_Run_WriteNewRun': {
                '/run/new': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/run/new',
                    'get_params': [
                        ],
                    },
                '/management/getinfo': {
                    'type': 'GET',
                    'url_pattern': '/management/getinfo',
                    'get_params': [
			'info_type=builds',
                        ],
                    },
                },
            'TestPlan_Cases_Run_Save': {
                '/run/new': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/run/new',
                    'get_params': [
                        ],
                    },
                },
            '@TestPlan_LoadMoreCases': {
                '/cases': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/cases/load-more',
                    'get_params': [
                        ],
                    },
                },
            'TestPlan_Cases_Run_AddCasesToRunPage': {
                '/plan/idnumber/chooseruns': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/plan/idnumber/chooseruns',
                    'get_params': [
			'type=case',
                        ],
                    },
                },
            'TestPlan_Cases_Run_AddCasesToRunUpdate': {
                '/plan/idnumber/chooseruns': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/plan/idnumber/chooseruns',
                    'get_params': [
                        ],
                    },
                'plan_planid': {
                    'type': 'GET',
                    'url_pattern': '/plan/idnumber/planName',
                    'get_params': [
                        ],
                    },
                'plan_id': {
                    'type': 'GET',
                    'url_pattern': '/plan/idnumber',
                    'get_params': [
                        ],
                    },
                'management_tags': {
                    'type': 'GET',
                    'url_pattern': '/management/tags',
                    'get_params': [
                        ],
                    },
                'plans_component': {
                    'type': 'GET',
                    'url_pattern': '/plans/component',
                    'get_params': [
                        ],
                    },
                'admins_jsi18n': {
                    'type': 'GET',
                    'url_pattern': '/admin/jsi18n',
                    'get_params': [
                        ],
                    },
                'cases': {
                    'type': 'POST',
                    'url_pattern': '/cases',
                    'get_params': [
                        ],
                    },
                },
            'TestPlan_Cases_Automated': {
                '/ajax/form': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/ajax/form',
                    'get_params': [
			'type=case',
                        ],
                    },
                },
            'TestPlan_Cases_AutomatedCommit': {
                '/cases/automated': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/cases/automated',
                    'get_params': [
                        ],
                    },
                '/cases': {
                    'type': 'POST',
                    'url_pattern': '/cases',
                    'get_params': [
                        ],
                    },
                },
            'TestPlan_Cases_DefaultTester': {
                '/management/getinfo': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/management/getinfo',
                    'get_params': [
			'info_type=users',
                        ],
                    },
                '/ajax/update': {
                    'type': 'POST',
                    'url_pattern': '/ajax/update',
                    'get_params': [
                        ],
                    },
                '/cases': {
                    'type': 'POST',
                    'url_pattern': '/cases',
                    'get_params': [
                        ],
                    },
                },
            'TestPlan_Cases_Component': {
                '/cases/component': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/cases/component',
                    'get_params': [
                        ],
                    },
                },
            'TestPlan_Cases_ComponentCommit': {
                '/cases/component': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/cases/component',
                    'get_params': [
                        ],
                    },
                '/cases': {
                    'type': 'POST',
                    'url_pattern': '/cases',
                    'get_params': [
                        ],
                    },
                },
            'TestPlan_Cases_Status': {
                '/ajax/update/case-status': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/ajax/update/case-status',
                    'get_params': [
                        ],
                    },
                '/cases': {
                    'type': 'POST',
                    'url_pattern': '/cases',
                    'get_params': [
                        ],
                    },
                },
            'TestPlan_Cases_Category': {
                '/cases/category': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/cases/category',
                    'get_params': [
                        ],
                    },
                },
            'TestPlan_Cases_CategoryUpdate': {
                '/cases': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/cases/category',
                    'get_params': [
                        ],
                    },
                },
            'TestPlan_Cases_Priority': {
                '/ajax/update/': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/ajax/update',
                    'get_params': [
                        ],
                    },
                '/cases': {
                    'type': 'POST',
                    'url_pattern': '/cases',
                    'get_params': [
                        ],
                    },
                },
            'TestRun_Open': {
                '/run/runid/': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/run/idnumber',
                    'get_params': [
                        ],
                    },
                },
            'CaseRun_ExpandCaseRun': {
                '/case/idnumber': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/case/idnumber',
                    'get_params': [
			'template_type=case_run',
                        ],
                    },
                },
            'CaseRun_AddComments': {
                '/comments/post': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/comments/post',
                    'get_params': [
                        ],
                    },
                '/case/caseid': {
                    'type': 'GET',
                    'url_pattern': '/case/idnumber',
                    'get_params': [
			'template_type=case_run',
                        ],
                    },
                '/case/caseid': {
                    'type': 'GET',
                    'url_pattern': '/case/idnumber',
                    'get_params': [
			'template_type=case_run',
                        ],
                    },
                },
            'CaseRun_AddBug': {
                '/caserun/idnumber/bug': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/caserun/idnumber/bug',
                    'get_params': [
			'a=add',
                        ],
                    },
                },
            'CaseRun_UpdateStatus': {
                '/ajax/update/case-run-status': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/ajax/update/case-run-status',
                    'get_params': [
                        ],
                    },
                '/case/idnumber': {
                    'type': 'GET',
                    'url_pattern': '/case/idnumber',
                    'get_params': [
			'template_type=case_run',
                        ],
                    },
                '/case/idnumber': {
                    'type': 'GET',
                    'url_pattern': '/case/idnumber',
                    'get_params': [
			'template_type=case_run',
                        ],
                    },
                },
            'TestRun_Filter': {
                '/run/id': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/run/idnumber',
                    'get_params': [
                        ],
                    },
                },
            'TestRun_Cases_Remove': {
                '/run/idnumber/removecaserun': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/run/idnumber/removecaserun',
                    'get_params': [
                        ],
                    },
                '/run/id': {
                    'type': 'GET',
                    'url_pattern': '/run/idnumber',
                    'get_params': [
                        ],
                    },
                },
            'TestRun_Cases_Add': {
                '/run/idnumber/assigncase': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/run/idnumber/assigncase',
                    'get_params': [
                        ],
                    },
                },
            'TestRun_Cases_AddUpdate': {
                '/run/idnumber/assigncase': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/run/idnumber/assigncase',
                    'get_params': [
                        ],
                    },
                '/run/idnumber': {
                    'type': 'GET',
                    'url_pattern': '/run/idnumber',
                    'get_params': [
                        ],
                    },
                },
            'TestRun_Assignee': {
                '/management/getinfo': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/management/getinfo',
                    'get_params': [
			'info_type=users'
                        ],
                    },
                '/ajax/update': {
                    'type': 'POST',
                    'url_pattern': '/ajax/update',
                    'get_params': [
                        ],
                    },
                '/run/idnumber': {
                    'type': 'GET',
                    'url_pattern': '/run/idnumber',
                    'get_params': [
                        ],
                    },
                },
            'TestRun_Re-order': {
                '/run/idnumber/ordercaserun': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/run/idnumber/ordercaserun',
                    'get_params': [
                        ],
                    },
                '/run/idnumber': {
                    'type': 'GET',
                    'url_pattern': '/run/idnumber',
                    'get_params': [
                        ],
                    },
                },
            'TestRun_Update': {
                '/run/idnumber/update': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/run/idnumber/update',
                    'get_params': [
                        ],
                    },
                '/run/idnumber': {
                    'type': 'GET',
                    'url_pattern': '/run/idnumber',
                    'get_params': [
                        ],
                    },
                },
            'TestRun_BuilkUpdateStatus': {
                '/ajax/update': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/ajax/update',
                    'get_params': [
                        ],
                    },
                '/run/idnumber': {
                    'type': 'GET',
                    'url_pattern': '/run/idnumber',
                    'get_params': [
                        ],
                    },
                },
            'CaseRun_BulkAddBug': {
                '/caserun/update-bugs-for-many': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/caserun/update-bugs-for-many',
                    'get_params': [
                        'action=add'
                        ],
                    },
                '/run/idnumber': {
                    'type': 'GET',
                    'url_pattern': '/run/idnumber',
                    'get_params': [
                        ],
                    },
                },
            'CaseRun_BulkAddComments': {
                '/caserun/comment-many': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/caserun/comment-many',
                    'get_params': [
                        ],
                    },
                '/run/idnumber': {
                    'type': 'GET',
                    'url_pattern': '/run/idnumber',
                    'get_params': [
                        ],
                    },
                },
            'TestRun_WriteNewRun': {
                '/run/new': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/run/new',
                    'get_params': [
                        ],
                    },
                '/management/getinfo': {
                    'type': 'GET',
                    'url_pattern': '/management/getinfo',
                    'get_params': [
			'info_type=builds',
                        ],
                    },
                },
            'TestRun_Save': {
                '/run/new': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/run/new',
                    'get_params': [
                        ],
                    },
                },
            'TestRun_Clone': {
                '/run/idnumber/clone': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/run/idnumber/clone',
                    'get_params': [
                        ],
                    },
                '/management/getinfo': {
                    'type': 'GET',
                    'url_pattern': '/management/getinfo',
                    'get_params': [
			'info_type=builds',
                        ],
                    },
                },
            '@TestRun_Save': {
                '/run/new': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/run/new',
                    'get_params': [
                        ],
                    },
                },
            'TestRun_Edit': {
                '/run/idnumber/edit/': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/run/idnumber/edit',
                    'get_params': [
                        ],
                    },
                '/management/getinfo': {
                    'type': 'GET',
                    'url_pattern': '/management/getinfo',
                    'get_params': [
			'info_type=buildes',
                        ],
                    },
                },
            'TestRun_EditSave': {
                '/run/idnumber/edit/': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/run/idnumber/edit',
                    'get_params': [
                        ],
                    },
                '/run/idnumber': {
                    'type': 'GET',
                    'url_pattern': '/run/idnumber',
                    'get_params': [
                        ],
                    },
                },
            'TestRun_Report': {
                '/run/idnumber/report/': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/run/idnumber/report',
                    'get_params': [
                        ],
                    },
                },
            #need update
            'TestRun_MyRuns': {
                '/runs': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/runs',
                    'get_params': [
                        ],
                    },
                '/runs/ajax/': {
                    'type': 'GET',
                    'url_pattern': '/runs/ajax',
                    'get_params': [
                        ],
                    },
                },
            'TestRun_Export': {
                '/run/runid/export': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/run/idnumber/export',
                    'get_params': [
                        ],
                    },
                },
            'TestPlan_Open': {
                '/plan/idnumber': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/plan/idnumber',
                    'get_params': [
                        ],
                    },
                '/plan/idnumber/planName': {
                    'type': 'GET',
                    'url_pattern': '/plan/idnumber/planName',
                    'get_params': [
                        ],
                    },
                'management_tags': {
                    'type': 'GET',
                    'url_pattern': '/management/tags',
                    'get_params': [
                        ],
                    },
                'plans_component': {
                    'type': 'GET',
                    'url_pattern': '/plans/component',
                    'get_params': [
                        ],
                    },
                'admins_jsi18n': {
                    'type': 'GET',
                    'url_pattern': '/admin/jsi18n',
                    'get_params': [
                        ],
                    },
                'cases': {
                    'type': 'POST',
                    'url_pattern': '/cases',
                    'get_params': [
                        ],
                    },
                },
            'TestCase_Open': {
                '/case/idnumber': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/case/idnumber',
                    'get_params': [
                        ],
                    },
                '/management/tags': {
                    'type': 'GET',
                    'url_pattern': '/management/tags',
                    'get_params': [
                        ],
                    },
                '/case/idnumber/plan': {
                    'type': 'GET',
                    'url_pattern': '/case/idnumber/plan',
                    'get_params': [
                        ],
                    },
                },
            'TestCase_Edit': {
                '/case/caseid/edit/': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/case/idnumber/edit',
                    'get_params': [
                        ],
                    },
                'admins_jsi18n': {
                    'type': 'GET',
                    'url_pattern': '/admin/jsi18n',
                    'get_params': [
                        ],
                    },
                },
            'TestCase_Save': {
                '/case/idnumber/edit': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/case/idnumber/edit',
                    'get_params': [
                        ],
                    },
                '/case/idnumber': {
                    'type': 'GET',
                    'url_pattern': '/case/idnumber',
                    'get_params': [
                        ],
                    },
                '/case/idnumber/plan': {
                    'type': 'GET',
                    'url_pattern': '/case/idnumber/plan',
                    'get_params': [
                        ],
                    },
                'management_tags': {
                    'type': 'GET',
                    'url_pattern': '/management/tags',
                    'get_params': [
                        ],
                    },
                },
            'TestCase_ClonePage': {
                '/cases/clone': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/cases/clone',
                    'get_params': [
                        ],
                    },
                },
            'TestCase_CloneFilterPlan': {
                '/plans': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/plans',
                    'get_params': [
			'action=clone_case',
                        ],
                    },
                },
            'TestCase_Clone': {
                '/cases/clone': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/cases/clone',
                    'get_params': [
                        ],
                    },
                '/case/idnumber': {
                    'type': 'GET',
                    'url_pattern': '/case/idnumber',
                    'get_params': [
                        ],
                    },
                'management_tags': {
                    'type': 'GET',
                    'url_pattern': '/management/tags',
                    'get_params': [
                        ],
                    },
                '/case/idnumber/plan': {
                    'type': 'GET',
                    'url_pattern': '/case/idnumber/plan',
                    'get_params': [
                        ],
                    },
                },
            'TestCase_StatusUpdate': {
                '/ajax/update/case-status': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/ajax/update/case-status',
                    'get_params': [
                        ],
                    },
                },
            'TestCase_WriteNew': {
                '/case/new/': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/case/new',
                    'get_params': [
                        ],
                    },
                'admins_jsi18n': {
                    'type': 'GET',
                    'url_pattern': '/admin/jsi18n',
                    'get_params': [
                        ],
                    },
                },
            'TestCase_Save_new': {
                '/case/new': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/case/new',
                    'get_params': [
                        ],
                    },
                'management_tags': {
                    'type': 'GET',
                    'url_pattern': '/management/tags',
                    'get_params': [
                        ],
                    },
                '/case/idnumber/plan': {
                    'type': 'GET',
                    'url_pattern': '/case/idnumber/plan',
                    'get_params': [
                        ],
                    },
                },
            'TestCase_AttachmentAdd': {
                '/case/idnumber/attachment': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/case/idnumber/attachment',
                    'get_params': [
                        ],
                    },
                },
            'TestCase_AttachmentUpload': {
                '/management/uploadfile': {
                    'main': True,
                    'type': 'POST',
                    'url_pattern': '/management/uploadfile',
                    'get_params': [
                        ],
                    },
                '/case/idnumber/attachment': {
                    'type': 'GET',
                    'url_pattern': '/case/idnumber/attachment',
                    'get_params': [
                        ],
                    },
                },
            'TestCase_AttachmentView': {
                '/management/checkfile/checkfileid': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/management/checkfile/checkfileid',
                    'get_params': [
                        ],
                    },
                },
            'TestCase_AttachmentDelete': {
                '/management/deletefile/checkfileid': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/management/deletefile/checkfileid',
                    'get_params': [
                        ],
                    },
                },
            'TestCase_TagAdd': {
                '/management/tags/': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/management/tags',
                    'get_params': [
			'a=add',
                        ],
                    },
                },
            'TestCase_TagRemove': {
                '/management/tags': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/management/tags',
                    'get_params': [
			'a=remove'
                        ],
                    },
                },
            'TestCase_BugAdd': {
                '/case/idnumber/bug': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/case/idnumber/bug',
                    'get_params': [
			'handle=add',
                        ],
                    },
                },
            'TestCase_BugRemove': {
                '/case/idnumber/bug': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/case/idnumber/bug',
                    'get_params': [
			'handle=remove',
                        ],
                    },
                },
            'TestCase_TestPlanAdd': {
                '/case/idnumber': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/case/idnumber',
                    'get_params': [
			'a=add'
                        ],
                    },
                },
            'TestCase_TestPlanRemove': {
                '/case/idnumber/plan': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/case/idnumber/plan',
                    'get_params': [
			'a=remove',
                        ],
                    },
                },
            'TestCase_CaseRun_ExpendPlan': {
                '/case/idnumber': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/case/idnumber',
                    'get_params': [
			'template_type=case_run_list',
                        ],
                    },
                },
            'TestCase_CaseRun_ViewCaseRun': {
                '/case/idnumber': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/case/idnumber',
                    'get_params': [
			'template_type=case_case_run',
                        ],
                    },
                },
            'QuickSearch_Plan': {
                '/plans': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/plans',
                    'get_params': [
			'a=search',
                        ],
                    },
                'admins_jsi18n': {
                    'type': 'GET',
                    'url_pattern': '/admin/jsi18n',
                    'get_params': [
                        ],
                    },
                '/plan/ajax': {
                    'type': 'GET',
                    'url_pattern': '/plan/ajax',
                    'get_params': [
			'a=search',
                        ],
                    },
                },
            'QuickSearch_Run': {
                '/runs': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/runs',
                    'get_params': [
			'a=search',
                        ],
                    },
                'admins_jsi18n': {
                    'type': 'GET',
                    'url_pattern': '/admin/jsi18n',
                    'get_params': [
                        ],
                    },
                'runs/ajax': {
                    'type': 'GET',
                    'url_pattern': '/runs/ajax',
                    'get_params': [
			'a=search',
                        ],
                    },
                },
            'QuickSearch_Case': {
                '/cases': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/cases',
                    'get_params': [
			'a=search',
                        ],
                    },
                'admins_jsi18n': {
                    'type': 'GET',
                    'url_pattern': '/admin/jsi18n',
                    'get_params': [
                        ],
                    },
                '/cases/ajax': {
                    'type': 'GET',
                    'url_pattern': '/cases/ajax',
                    'get_params': [
			'a=search',
                        ],
                    },
                },
            'SearchPlans_Open': {
                '/plans': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/plans',
                    'get_params': [
                        ],
                    },
                'admins_jsi18n': {
                    'type': 'GET',
                    'url_pattern': '/admin/jsi18n',
                    'get_params': [
                        ],
                    },
                },
            'SearchPlans_Search': {
                '/plans': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/plans',
                    'get_params': [
			'action=search',
                        ],
                    },
                'admins_jsi18n': {
                    'type': 'GET',
                    'url_pattern': '/admin/jsi18n',
                    'get_params': [
                        ],
                    },
                '/plan/ajax': {
                    'type': 'GET',
                    'url_pattern': '/plan/ajax',
                    'get_params': [
			'action=search',
                        ],
                    },
                },
            'SearchRuns_Open': {
                '/runs': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/runs',
                    'get_params': [
                        ],
                    },
                },
            'SearchRuns_Search': {
                '/runs': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/runs',
                    'get_params': [
			'action=search',
                        ],
                    },
                '/runs/ajax': {
                    'type': 'GET',
                    'url_pattern': '/runs/ajax',
                    'get_params': [
			'action=search',
                        ],
                    },
                },
            'SearchCases_Open': {
                '/cases/search': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/cases/search',
                    'get_params': [
                        ],
                    },
                },
            'SearchCases_Search': {
                '/cases/search': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/cases/search',
                    'get_params': [
                        ],
                    },
                '/cases/ajax': {
                    'type': 'GET',
                    'url_pattern': '/cases/ajax',
                    'get_params': [
                        ],
                    },
                },
            'AdvanceSearch_Open': {
                '/advance-search': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/advance-search',
                    'get_params': [
                        ],
                    },
                'admins_jsi18n': {
                    'type': 'GET',
                    'url_pattern': '/admin/jsi18n',
                    'get_params': [
                        ],
                    },
                },
            'AdvanceSearch_TestPlan': {
                '/advance-search': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/advance-search',
                    'get_params': [
			'target=plan',
                        ],
                    },
                },
            'AdvanceSearch_TestRun': {
                '/advance-search': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/advance-search',
                    'get_params': [
			'target=run',
                        ],
                    },
                },
            'AdvanceSearch_TestCase': {
                '/advance-search': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/advance-search',
                    'get_params': [
			'target=case',
                        ],
                    },
                },
            'Reporting_OR_OpenOverallReport': {
                '/report/overall': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/report/overall',
                    'get_params': [
                        ],
                    },
                },
            'Reporting_OR_Product': {
                '/report/product/idnumber/overview': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/report/product/idnumber/overview',
                    'get_params': [
                        ],
                    },
                },
            'Reporting_OR_Versions': {
                '/report/product/idnumber/version': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/report/product/idnumber/version',
                    'get_params': [
                        ],
                    },
                },
            'Reporting_OR_VersionDetail': {
                '/report/product/idnumber/version': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/report/product/idnumber/version',
                    'get_params': [
                        ],
                    },
                },
            'Reporting_OR_Builds': {
                '/report/product/idnumber/build': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/report/product/idnumber/build',
                    'get_params': [
                        ],
                    },
                },
            'Reporting_OR_Components': {
                '/report/product/idnumber/component': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/report/product/idnumber/component',
                    'get_params': [
                        ],
                    },
                },
            'Reporting_CR_OpenCustomReport': {
                '/report/custom': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/report/custom',
                    'get_params': [
                        ],
                    },
                },
            'Reporting_CR_Search': {
                '/report/custom': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/report/custom',
                    'get_params': [
			'a=Search',
                        ],
                    },
                '/management/getinfo/': {
                    'type': 'GET',
                    'url_pattern': '/management/getinfo',
                    'get_params': [
			'info_type=builds',
                        ],
                    },
                },
            'Reporting_CR_Detail': {
                '/report/custom/details': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/report/custom/details',
                    'get_params': [
			'a=Search',
                        ],
                    },
                '/management/getinfo/': {
                    'type': 'GET',
                    'url_pattern': '/management/getinfo',
                    'get_params': [
                'info_type=builds',
                        ],
                    },
                },
            'Reporting_TR_OpenTestingReport': {
                '/report/testing/': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/report/testing',
                    'get_params': [
                        ],
                    },
                '/admin/jsi18n': {
                    'type': 'GET',
                    'url_pattern': '/admin/jsi18n',
                    'get_params': [
                        ],
                    },
                },
            'Reporting_TR_SelectProduct': {
                '/ajax/get-prod-relate-obj': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/ajax/get-prod-relate-obj',
                    'get_params': [
			'target=version',
                        ],
                    },
                '/ajax/get-prod-relate-obj': {
                    'type': 'GET',
                    'url_pattern': '/ajax/get-prod-relate-obj',
                    'get_params': [
			'target=builds',
                        ],
                    },
                },
            'Reporting_TR_GenerateReport(ByCase-RunTester)': {
                '/report/testing/': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/report/testing',
                    'get_params': [
			'report_type=per_build_report',
                        ],
                    },
                '/admin/jsi18n': {
                    'type': 'GET',
                    'url_pattern': '/admin/jsi18n',
                    'get_params': [
                        ],
                    },
                },
            'Reporting_TR_GenerateReport(ByCasePriority)': {
                '/report/testing/': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/report/testing',
                    'get_params': [
			'report_type=per_priority_report',
                        ],
                    },
                '/admin/jsi18n': {
                    'type': 'GET',
                    'url_pattern': '/admin/jsi18n',
                    'get_params': [
                        ],
                    },
                },
            'Reporting_TR_GenerateReport(ByPlanTag)': {
                '/report/testing/': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/report/testing',
                    'get_params': [
			'report_type=runs_with_rates_per_plan_tag',
                        ],
                    },
                '/admin/jsi18n': {
                    'type': 'GET',
                    'url_pattern': '/admin/jsi18n',
                    'get_params': [
                        ],
                    },
                },
            'Reporting_TR_GenerateReport(ByPlan&Build)': {
                '/report/testing/': {
                    'main': True,
                    'type': 'GET',
                    'url_pattern': '/report/testing',
                    'get_params': [
			'report_type=runs_with_rates_per_plan_build',
                        ],
                    },
                '/admin/jsi18n': {
                    'type': 'GET',
                    'url_pattern': '/admin/jsi18n',
                    'get_params': [
                        ],
                    },
                },
            }
    return res

if __name__ == "__main__":
    main()

